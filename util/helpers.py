import requests, json, csv


def test():
    print("test")


def scrape_urls(mol_formula):
    url = (
        "https://mona.fiehnlab.ucdavis.edu/rest/spectra/search?page=0&query=compound.metaData%3Dq%3D%27"
        "name%3D%3D%22molecular+formula%22+and+value%3Dmatch%3D%22.*"
        + mol_formula
        + ".*%22%27&text="
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


def remove_commas(row):
    res = []
    for item in row:
        res.append(
            str(item).replace(",", ";").replace("rest/spectra", "spectra/display")
        )
    return res


def scrape_compound(url):
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


def scrape(file_name):
    # reading the input molecular formulas
    with open(file_name) as file:
        # with open("MoNa_compounds_molformula.csv", "r") as file:
        lines = file.read()
    lines = lines.split("\n")

    # writing the output header in output file
    with open("test.csv", "a") as f:
        csv.writer(f).writerow(
            [
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

    for formula in lines:
        ids = scrape_urls(formula)
        for id in ids:
            url = "https://mona.fiehnlab.ucdavis.edu/rest/spectra/" + str(id)
            row = scrape_compound(url)
            if row is not None and len(row) > 0:
                row = remove_commas(row)
            else:
                row = [url]
            with open("test.csv", "a") as f:
                try:
                    csv.writer(f).writerow(row)
                except Exception as e:
                    print(e)
