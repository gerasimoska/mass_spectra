var app = new Vue({
    el: '#app',
    delimiters : ['[[',']]'],
    data: {
        options: {
            'ion_mode': [
                {
                    id: 'positive',
                    text: 'Positive',
                    value: false
                },
                {
                    id: 'negative',
                    text: 'Negative',
                    value: false
                }
            ],
            'ms_type': [
                {
                    id: 'ms1',
                    text: 'MS1',
                    value: false
                },

                {
                    id: 'ms2',
                    text: 'MS2',
                    value: false
                },

                {
                    id: 'ms3',
                    text: 'MS3',
                    value: false
                },

                {
                    id: 'ms4',
                    text: 'MS4',
                    value: false
                }
            ],
            'source_introduction': [
                {
                    id: 'lc',
                    text: 'Liquid Chromatography (LC)',
                    value: false
                },
                {
                    id: 'gc',
                    text: 'Gas Chromatography (GC)',
                    value: false
                },
                {
                    id: 'ce',
                    text: 'Capillary Electrophoresis (CE)',
                    value: false
                }
            ],
            'other_instrument_types': [
                {
                    id: 'apci_itft',
                    text: 'APCI-ITFT',
                    value: false
                },
                {
                    id: 'apci_ittof',
                    text: 'APCI-ITTOF',
                    value: false
                },
                {
                    id: 'apci_q',
                    text: 'APCI-Q',
                    value: false
                },
                {
                    id: 'ci_b',
                    text: 'CI-B',
                    value: false
                },
                {
                    id: 'ci_q',
                    text: 'CI-Q',
                    value: false
                },
                {
                    id: 'fab_b',
                    text: 'FAB-B',
                    value: false
                },
                {
                    id: 'fab_be',
                    text: 'FAB-BE',
                    value: false
                },
                {
                    id: 'fab_eb',
                    text: 'FAB-EB',
                    value: false
                },
                {
                    id: 'fd_b',
                    text: 'FD-B',
                    value: false
                },
                {
                    id: 'fi_b',
                    text: 'FI-B',
                    value: false
                },
                {
                    id: 'gc_apci_qtof',
                    text: 'GC-APCI-QTOF',
                    value: false
                },
                {
                    id: 'gc_fi_tof',
                    text: 'GC-FI-TOF',
                    value: false
                },
                {
                    id: 'lc_apci_itft',
                    text: 'LC-APCI-ITFT',
                    value: false
                },
                {
                    id: 'lc_apci_q',
                    text: 'LC-APCI-Q',
                    value: false
                },
                {
                    id: 'lc_apci_qtof',
                    text: 'LC-APCI-QTOF',
                    value: false
                },
                {
                    id: 'lc_appi_qq',
                    text: 'LC-APPI-QQ',
                    value: false
                },
                {
                    id: 'maldi-qit',
                    text: 'MALDI-QIT',
                    value: false
                },
                {
                    id: 'maldi_qittof',
                    text: 'MALDI-QITTOF',
                    value: false
                },
                {
                    id: 'maldi_tof',
                    text: 'MALDI-TOF',
                    value: false
                },
                {
                    id: 'maldi_toftof',
                    text: 'MALDI-TOFTOF',
                    value: false
                },
                {
                    id: 'si_be',
                    text: 'SI-BE',
                    value: false
                }
            ],
            'library': [
                {
                    id: 'lipidblast',
                    text: 'LipidBlast',
                    value: false
                },
                {
                    id: 'massbank',
                    text: 'MassBank',
                    value: false
                },
                {
                    id: 'vf_npl',
                    text: 'VF-NPL',
                    value: false
                },
                {
                    id: 'gnps',
                    text: 'GNPS',
                    value: false
                },
                {
                    id: 'riken_plasma',
                    text: 'RIKEN PlaSMA',
                    value: false
                },
                {
                    id: 'respect',
                    text: 'ReSpect',
                    value: false
                },
                {
                    id: 'fahfa',
                    text: 'FAHFA',
                    value: false
                },
                {
                    id: 'fiehn_hilic',
                    text: 'Fiehn HILIC',
                    value: false
                },
                {
                    id: 'metabobase',
                    text: 'MetaboBASE',
                    value: false
                },
                {
                    id: 'fiehnlib',
                    text: 'FiehnLib',
                    value: false
                },
                {
                    id: 'pathogenbox',
                    text: 'PathogenBox',
                    value: false
                },
                {
                    id: 'riken_oxpls',
                    text: 'RIKEN OxPLs',
                    value: false
                },
                {
                    id: 'volatile_fiehnlib',
                    text: 'Volatile FiehnLib',
                    value: false
                }
            ],
            'input_type': [
                {
                    id: 'inchi_key',
                    text: 'InChi Key',
                    value: false
                },
                {
                    id: 'molecular_formula',
                    text: 'Molecular Formula',
                    value: false
                },
                {
                    id: 'exact_mass',
                    text: 'Exact Mass',
                    value: false,
                    input: null
                }
            ],
            'mass_spectra_library': [
                {
                    id: 'mona',
                    text: 'MoNa'
                },
                {
                    id: 'massbank_of_europe',
                    text: 'MassBank of Europe'
                }
            ]
        },
        request: {}
    },
    mounted () {
        axios
          .get('https://api.coindesk.com/v1/bpi/currentprice.json')
          .then(response => (this.info = response))
    },
    methods: {
        submit(event){
        axios({
                method : "POST",
                url:"{% 'search' %}", //django path name
                headers: {'X-CSRFTOKEN': '{{ csrf_token }}', 'Content-Type': 'application/json'},
                data : {"username":this.options},//data
              }).then(response => {
                  console.log("success")
                  console.log(response)
              }).catch(err => {
                     console.log(err)
              });
        }
    }
})