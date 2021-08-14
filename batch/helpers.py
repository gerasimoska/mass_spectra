import requests, json, csv
from bs4 import BeautifulSoup


def scrape_urls_MoNa(
    inputType, tolerance, input_item, ionMode, msType, sourceIntroduction, library
):
    if tolerance is None:
        tolerance = 0
    if len(ionMode) == 0:
        url_ionMode = ""
    elif len(ionMode) == 1:
        url_ionMode = (
            '+and+(metaData=q=\'name=="ionization+mode"+and+value=="'
            + str(ionMode[0])
            + "\"')"
        )
    else:
        url_ionMode = (
            '+and+(metaData=q=\'name=="ionization+mode"+and+value=="positive"\'+or+'
            'metaData=q=\'name=="ionization+mode"+and+value=="negative"\')'
        )

    if len(msType) == 0:
        url_msType = ""
    elif len(msType) == 1:
        url_msType = (
            '+and+(metaData=q=\'name=="ms+level"+and+value=="' + str(msType[0]) + "\"')"
        )
    else:
        url_msType = (
            '+and+(metaData=q=\'name=="ms+level"+and+value=="' + str(msType[0]) + "\"'"
        )
        for ms in msType[1:]:
            url_msType += (
                '+or+metaData=q=\'name=="ms+level"+and+value=="' + str(ms) + "\"'"
            )
        url_msType += ")"

    if len(sourceIntroduction) == 0:
        url_sourceIntroduction = ""
    elif len(sourceIntroduction) == 1:
        url_sourceIntroduction = (
            '+and+(tags.text=="' + str(sourceIntroduction[0]) + '") '
        )
    else:
        url_sourceIntroduction = '+and+(tags.text=="' + str(sourceIntroduction[0]) + '"'
        for s in sourceIntroduction[1:]:
            url_sourceIntroduction += '+or+tags.text=="' + str(s) + '"'
        url_sourceIntroduction += ") "

    if len(library) == 0:
        url_library = ""
    elif len(library) == 1:
        url_library = '+and+(tags.text=="' + str(library[0]).replace(" ","+") + '")'
    else:
        url_library = '+and+(tags.text=="' + str(library[0]).replace(" ","+") + '"'
        for l in library[1:]:
            url_library += '+or+tags.text=="' + str(l).replace(" ","+") + '"'
        url_library += ")"
    if "molFormula" in inputType:
        url = (
            "https://mona.fiehnlab.ucdavis.edu/rest/spectra/search?page=0&query=compound.metaData%3Dq%3D%27name%3D"
            "%3D%22molecular+formula%22+and+value%3Dmatch%3D%22.*"
            + input_item
            + ".*%22%27"
            + url_sourceIntroduction
            + url_ionMode
            + url_msType
            + url_library
            + "&text= "
        )
    elif "inchiKey" in inputType:
        url = (
            "https://mona.fiehnlab.ucdavis.edu/rest/spectra/search?page=0&query=compound.metaData=q='name"
            '=="InChIKey"+and+value=="'
            + input_item
            + "%22%27"
            + url_sourceIntroduction
            + url_ionMode
            + url_msType
            + url_library
            + "&text= "
        )
    else:
        url = (
            "https://mona.fiehnlab.ucdavis.edu/rest/spectra/search?page=0&query=compound.metaData=q='name==\"total "
            'exact+mass"+and+value>= '
            + str(float(input_item) - float(tolerance))
            + "+and+value <= "
            + str(float(input_item) + float(tolerance))
            + "'"
            + url_sourceIntroduction
            + url_ionMode
            + url_msType
            + url_library
            + "&text="
        )
    try:
        res = json.loads(requests.get(url).content.decode("utf-8"))
    except Exception as e:
        print(e)
        return []
    ids = []
    for item in res:
        ids.append(item.get("id"))
    return ids


def scrape_urls_MassBankEurope(
    inputType,
    tolerance,
    input_item,
    ionMode,
    msType,
    sourceIntroduction,
    instrumentTypes,
):
    url_msType = ""
    if len(msType) > 0:
        for ms in msType:
            url_msType += "&ms=" + str(ms).replace("1", "")
    url_ionMode = ""
    if len(ionMode) == 1:
        for ion in ionMode:
            url_ionMode += "&ion=" + str(ion).replace("positive", "1").replace(
                "negative", "-1"
            )
    elif len(ionMode) == 2:
        url_ionMode = "&ion=0"
    url_insType = ""
    if len(sourceIntroduction) > 0:
        if "GC-MS" in sourceIntroduction:
            url_insType += "&inst_grp=EI&inst=EI-B&inst=EI-EBEB&inst=GC-EI-Q&inst=GC-EI-QQ&inst=GC-EI-TOF"
        if "LC-MS" in sourceIntroduction:
            url_insType += (
                "&inst_grp=ESI&inst=CE-ESI-TOF&inst=ESI-ITFT&inst=ESI-ITTOF&inst=ESI-QIT&inst=ESI-QTOF"
                "&inst=ESI-TOF&inst=LC-ESI-IT&inst=LC-ESI-ITFT&inst=LC-ESI-ITTOF&inst=LC-ESI-Q&inst=LC-ESI"
                "-QFT&inst=LC-ESI-QIT&inst=LC-ESI-QQ&inst=LC-ESI-QQQ&inst=LC-ESI-QTOF&inst=LC-ESI-TOF "
            )
    for ins in instrumentTypes:
        url_insType += "&inst=" + str(ins)

    if "molFormula" in inputType:
        url = (
            "https://massbank.eu/MassBank/Result.jsp?compound=&op1=and&mz=&tol="
            + str(tolerance)
            + "&op2=and&formula="
            + input_item
            + "&type=quick&searchType=keyword&sortKey=not&sortAction=1&pageNo=1&exec="
            + url_insType
            + url_msType
            + url_ionMode
        )
    elif "inchiKey" in inputType:
        url = (
            "https://massbank.eu/MassBank/Result.jsp?inchikey="
            + input_item
            + "&type=inchikey&searchType=inchikey&sortKey=not&sortAction=1&pageNo=1&exec="
            + url_insType
            + url_msType
            + url_ionMode
        )
    else:
        url = (
            "https://massbank.eu/MassBank/Result.jsp?compound=&op1=and&mz="
            + input_item
            + "&tol="
            + str(tolerance)
            + "&op2=and&formula=&type=quick&searchType=keyword&sortKey=not&sortAction=1&pageNo=1&exec="
            + url_insType
            + url_msType
            + url_ionMode
        )
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
    except Exception as e:
        print(e)
        return []
    ids = []
    for elem in soup.find_all("a", class_="preview_structure", href=True):
        ids.append(str(elem["href"]).split("_")[-2])
    return ids


def remove_commas(row):
    res = []
    for item in row:
        res.append(
            str(item).replace(",", ";").replace("rest/spectra", "spectra/display")
        )
    return res


def scrape_compound_MoNa(url):
    try:
        res = json.loads(requests.get(url).content.decode("utf-8"))
    except Exception as e:
        print(e)
        return
    name = res.get("compound")[0].get("names")[0].get("name")
    splash = res.get("splash").get("splash")
    ions = res.get("spectrum").replace(" ", " | ").replace(":", " ")
    total_exact_mass = smiles = pubChem = molecular_formula = inChIKey = inChI = ""
    for item in res.get("compound")[0].get("metaData"):
        if item.get("name") == "PubChem":
            pubChem = item.get("value")
        elif item.get("name") == "InChI":
            inChI = item.get("value")
        elif item.get("name") == "InChIKey":
            inChIKey = item.get("value")
        elif item.get("name") == "molecular formula":
            molecular_formula = item.get("value")
        elif item.get("name") == "total exact mass":
            total_exact_mass = item.get("value")
        elif item.get("name") == "SMILES":
            smiles = item.get("value")
    author = (
        column
    ) = (
        column_temperature
    ) = (
        data_transformation
    ) = (
        derivatization_mass
    ) = (
        derivatization_type
    ) = (
        detector_voltage
    ) = (
        flow_rate
    ) = (
        guard_column
    ) = (
        injection
    ) = (
        injection_temperature
    ) = (
        injection_volume
    ) = (
        instrument
    ) = (
        instrument_type
    ) = (
        ion_source_temperature
    ) = (
        ionization_energy
    ) = (
        ionization_mode
    ) = (
        mobile_phase
    ) = (
        ms_level
    ) = oven_temperature = retention_index = scan_range = transfer_line_temperature = ""
    for item in res.get("metaData"):
        if item.get("name") == "author":
            author = item.get("value")
        if item.get("name") == "column":
            column = item.get("value")
        elif item.get("name") == "column temperature":
            column_temperature = item.get("value")
        elif item.get("name") == "data transformation":
            data_transformation = item.get("value")
        elif item.get("name") == "derivatization mass":
            derivatization_mass = item.get("value")
        elif item.get("name") == "derivatization type":
            derivatization_type = item.get("value")
        elif item.get("name") == "detector voltage":
            detector_voltage = item.get("value")
        elif item.get("name") == "flow rate":
            flow_rate = item.get("value")
        elif item.get("name") == "guard column":
            guard_column = item.get("value")
        elif item.get("name") == "injection":
            injection = item.get("value")
        elif item.get("name") == "injection temperature":
            injection_temperature = item.get("value")
        elif item.get("name") == "injection volume":
            injection_volume = item.get("value")
        elif item.get("name") == "instrument":
            instrument = item.get("value")
        elif item.get("name") == "instrument type":
            instrument_type = item.get("value")
        elif item.get("name") == "ion source temperature":
            ion_source_temperature = item.get("value")
        elif item.get("name") == "ionization energy":
            ionization_energy = item.get("value")
        elif item.get("name") == "ionization mode":
            ionization_mode = item.get("value")
        elif item.get("name") == "mobile phase":
            mobile_phase = item.get("value")
        elif item.get("name") == "ms level":
            ms_level = item.get("value")
        elif item.get("name") == "oven temperature":
            oven_temperature = item.get("value")
        elif item.get("name") == "retention index":
            retention_index = item.get("value")
        elif item.get("name") == "scan range":
            scan_range = item.get("value")
        elif item.get("name") == "transfer line temperature":
            transfer_line_temperature = item.get("value")
    return (
        str(url),
        name,
        ions,
        splash,
        total_exact_mass,
        smiles,
        pubChem,
        molecular_formula,
        inChIKey,
        inChI,
        author,
        column,
        column_temperature,
        data_transformation,
        derivatization_mass,
        derivatization_type,
        detector_voltage,
        flow_rate,
        guard_column,
        injection,
        injection_temperature,
        injection_volume,
        instrument,
        instrument_type,
        ion_source_temperature,
        ionization_energy,
        ionization_mode,
        mobile_phase,
        ms_level,
        oven_temperature,
        retention_index,
        scan_range,
        transfer_line_temperature,
    )


def scrape_compound_MassBankEurope(url):
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
    except Exception as e:
        print(e)
        return []
    inChIKey = instrument = instrumentType = msType = ionMode = collisionEnergy = ""
    res = json.loads(
        str(soup.find("script", type="application/ld+json"))
        .split(">")[1]
        .split("</")[0]
        .strip()
    )
    res_js = json.loads(
        str(soup.find("script", type="text/javascript"))
        .split("var data=")[1]
        .split("</")[0]
        .strip()
        .replace(";", "")
    )
    name = res[0].get("name")
    ions = []
    tmp = res_js.get("peaks")
    for peak in tmp:
        ions.append(str(peak.get("intensity")) + " " + str(peak.get("mz")) + " | ")
    ions = (
        str(ions)
        .replace("'", "")
        .replace(",", "")
        .replace(" | ]", "")
        .replace("[", "")
        .replace("  ", " ")
        .strip()
    )
    total_exact_mass = res[0].get("monoisotopicMolecularWeight")
    smiles = res[0].get("smiles")
    molecularFormula = res[0].get("molecularFormula")
    inChI = str(res[0].get("inChI")).replace("InChI=", "")
    if (
        len(
            str(soup.find_all("div", class_="w3-padding")).split(
                "INCHIKEY <a href='https://www.google.com/search?q=\""
            )
        )
        > 1
    ):
        inChIKey = (
            str(soup.find_all("div", class_="w3-padding"))
            .split("INCHIKEY <a href='https://www.google.com/search?q=\"")[1]
            .split('"')[0]
            .strip()
        )
    if (
        len(
            str(soup.find_all("div", class_="w3-padding")).split(
                "<b>AC$INSTRUMENT_TYPE:</b>"
            )
        )
        > 0
    ):
        instrument = (
            str(soup.find_all("div", class_="w3-padding"))
            .split("<b>AC$INSTRUMENT:</b>")[1]
            .split("<br/>")[0]
            .strip()
        )
    if (
        len(
            str(soup.find_all("div", class_="w3-padding")).split(
                "<b>AC$INSTRUMENT_TYPE:</b>"
            )
        )
        > 0
    ):
        instrumentType = (
            str(soup.find_all("div", class_="w3-padding"))
            .split("<b>AC$INSTRUMENT_TYPE:</b>")[1]
            .split("<br/>")[0]
            .strip()
        )
    if (
        len(
            str(soup.find_all("div", class_="w3-padding")).split(
                "<b>MASS_SPECTROMETRY:</b>"
            )
        )
        > 1
    ):
        msType = (
            str(soup.find_all("div", class_="w3-padding"))
            .split("<b>AC$MASS_SPECTROMETRY:</b>")[1]
            .split("<br/>")[0]
            .strip()
        )
    if (
        len(
            str(soup.find_all("div", class_="w3-padding")).split(
                "<b>AC$MASS_SPECTROMETRY:</b>"
            )
        )
        > 2
    ):
        ionMode = (
            str(soup.find_all("div", class_="w3-padding"))
            .split("<b>AC$MASS_SPECTROMETRY:</b>")[2]
            .split("<br/>")[0]
            .strip()
        )
    if (
        len(
            str(soup.find_all("div", class_="w3-padding")).split(
                "<b>AC$MASS_SPECTROMETRY:</b>"
            )
        )
        > 3
    ):
        collisionEnergy = (
            str(soup.find_all("div", class_="w3-padding"))
            .split("<b>AC$MASS_SPECTROMETRY:</b>")[3]
            .split("<br/>")[0]
            .strip()
        )
    return (
        str(url),
        name,
        ions,
        total_exact_mass,
        smiles,
        molecularFormula,
        inChI,
        inChIKey,
        instrument,
        instrumentType,
        msType,
        ionMode,
        collisionEnergy,
    )


def scrape(
    fileName,
    ionMode,
    msType,
    sourceIntroduction,
    instrumentTypes,
    library,
    inputType,
    tolerance,
    massSpectraLibrary,
):
    # reading the input molecular formulas
    with open(str(fileName), "r", encoding='utf-8-sig') as file:
        lines = file.read()
    lines = lines.split("\n")

    # writing the output header in output file
    with open(str(fileName).replace(".csv", "_output.csv"), "a") as f:
        if "mona" in massSpectraLibrary:
            if "molFormula" in inputType:
                csv.writer(f).writerow(
                    [
                        "input molecular formula",
                        "url",
                        "name",
                        "ions",
                        "splash",
                        "total_exact_mass",
                        "smiles",
                        "pubChem",
                        "molecular_formula",
                        "InChIKey",
                        "InChI",
                        "author",
                        "column",
                        "column_temperature",
                        "data_transformation",
                        "derivatization_mass",
                        "derivatization_type",
                        "detector_voltage",
                        "flow_rate",
                        "guard_column",
                        "injection",
                        "injection_temperature",
                        "injection_volume",
                        "instrument",
                        "instrument_type",
                        "ion_source_temperature",
                        "ionization_energy",
                        "ionization_mode",
                        "mobile_phase",
                        "ms_level",
                        "oven_temperature",
                        "retention_index",
                        "scan_range",
                        "transfer_line_temperature",
                    ]
                )
            elif "inchiKey" in inputType:
                csv.writer(f).writerow(
                    [
                        "input InChi Key",
                        "url",
                        "name",
                        "ions",
                        "splash",
                        "total_exact_mass",
                        "smiles",
                        "pubChem",
                        "molecular_formula",
                        "InChIKey",
                        "InChI",
                        "author",
                        "column",
                        "column_temperature",
                        "data_transformation",
                        "derivatization_mass",
                        "derivatization_type",
                        "detector_voltage",
                        "flow_rate",
                        "guard_column",
                        "injection",
                        "injection_temperature",
                        "injection_volume",
                        "instrument",
                        "instrument_type",
                        "ion_source_temperature",
                        "ionization_energy",
                        "ionization_mode",
                        "mobile_phase",
                        "ms_level",
                        "oven_temperature",
                        "retention_index",
                        "scan_range",
                        "transfer_line_temperature",
                    ]
                )
            elif "exactMass" in inputType:
                csv.writer(f).writerow(
                    [
                        "input exact mass",
                        "url",
                        "name",
                        "ions",
                        "splash",
                        "total_exact_mass",
                        "smiles",
                        "pubChem",
                        "molecular_formula",
                        "InChIKey",
                        "InChI",
                        "author",
                        "column",
                        "column_temperature",
                        "data_transformation",
                        "derivatization_mass",
                        "derivatization_type",
                        "detector_voltage",
                        "flow_rate",
                        "guard_column",
                        "injection",
                        "injection_temperature",
                        "injection_volume",
                        "instrument",
                        "instrument_type",
                        "ion_source_temperature",
                        "ionization_energy",
                        "ionization_mode",
                        "mobile_phase",
                        "ms_level",
                        "oven_temperature",
                        "retention_index",
                        "scan_range",
                        "transfer_line_temperature",
                    ]
                )

        if "massbank_of_europe" in massSpectraLibrary:
            if "molFormula" in inputType:
                csv.writer(f).writerow(
                    [
                        "input molecular formula",
                        "url",
                        "name",
                        "ions",
                        "total_exact_mass",
                        "smiles",
                        "molecularFormula",
                        "inChI",
                        "inChI Key",
                        "instrument",
                        "instrumentType",
                        "msType",
                        "ionMode",
                        "collisionEnergy",
                    ]
                )
            elif "inchiKey" in inputType:
                csv.writer(f).writerow(
                    [
                        "input InChi Key",
                        "url",
                        "name",
                        "ions",
                        "total_exact_mass",
                        "smiles",
                        "molecularFormula",
                        "inChI",
                        "inChI Key",
                        "instrument",
                        "instrumentType",
                        "msType",
                        "ionMode",
                        "collisionEnergy",
                    ]
                )
            elif "exactMass" in inputType:
                csv.writer(f).writerow(
                    [
                        "input exact mass",
                        "url",
                        "name",
                        "ions",
                        "total_exact_mass",
                        "smiles",
                        "molecularFormula",
                        "inChI",
                        "inChI Key",
                        "instrument",
                        "instrumentType",
                        "msType",
                        "ionMode",
                        "collisionEnergy",
                    ]
                )

    for input_item in lines:
        if len(input_item.replace(" ", "")) > 0:
            if "mona" in massSpectraLibrary:
                ids = scrape_urls_MoNa(
                    inputType,
                    tolerance,
                    input_item,
                    ionMode,
                    msType,
                    sourceIntroduction,
                    library,
                )
                if len(ids) > 0:
                    for id in ids:
                        url = "https://mona.fiehnlab.ucdavis.edu/rest/spectra/" + str(
                            id
                        )
                        row = scrape_compound_MoNa(url)
                        if row is not None and len(row) > 0:
                            row = remove_commas(row)
                        else:
                            row = [url]
                        with open(
                            str(fileName).replace(".csv", "_output.csv"), "a"
                        ) as f:
                            row.insert(0, str(input_item))
                            csv.writer(f).writerow(row)
                else:
                    row = [input_item, "No URL found"]
                    with open(str(fileName).replace(".csv", "_output.csv"), "a") as f:
                        csv.writer(f).writerow(row)
            if "massbank_of_europe" in massSpectraLibrary:
                ids = scrape_urls_MassBankEurope(
                    inputType,
                    tolerance,
                    input_item,
                    ionMode,
                    msType,
                    sourceIntroduction,
                    instrumentTypes,
                )
                if len(ids) > 0:
                    for id in ids:
                        url = "https://massbank.eu/MassBank/RecordDisplay?id=" + str(id)
                        row = scrape_compound_MassBankEurope(url)
                        if row is not None and len(row) > 0:
                            row = remove_commas(row)
                        else:
                            row = [url]
                        with open(
                            str(fileName).replace(".csv", "_output.csv"), "a"
                        ) as f:
                            row.insert(0, str(input_item))
                            csv.writer(f).writerow(row)
                else:
                    row = [input_item, "No URL found"]
                    with open(str(fileName).replace(".csv", "_output.csv"), "a") as f:
                        csv.writer(f).writerow(row)
