import yara


def yaraScan(email):
    matches = []
    rules = yara.compile(filepaths={    #compilar un conjunto de reglas
      'namespace1':'rules/testRule1.ya',
      'namespace2':'rules/testRule2.ya'
    })

    reglas = rules.match(data = email)  #datos a analizar

    for match in reglas:    #las reglas que se cumplan las guardamos en un array
        matches.append({"name": match.rule, "meta": match.meta})


    return (matches)