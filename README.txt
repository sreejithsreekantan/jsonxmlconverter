=================================
		JSON XML CONVERTER
=================================

JSONXMLCONVERTER is a python module to read json files and created xml files
out of it. 
Typical usage looks like this:
	#!/usr/bin/env python

    from jsonxmlconverter import jsonxmlconverter
    
    inputfile = "1.json"
    outputfile = "1.xml"
    j = jsonxmlconverter(inputfile)
	out = open(outputfile, 'w')
	j.setIndent("\t") # set indentation to "\t"
	j.generateXMLFile(outputfile)

	-------------------------------------------------------------------------
	Input file(1.json):
		{
		    "glossary": {
		        "title": "example glossary",
				"GlossDiv": {
		            "title": "S",
					"GlossList": {
		                "GlossEntry": {
		                    "ID": "SGML",
							"SortAs": "SGML",
							"GlossTerm": "Standard Generalized Markup Language",
							"Acronym": "SGML",
							"Abbrev": "ISO 8879:1986",
							"GlossDef": {
		                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
								"GlossSeeAlso": ["GML", "XML"]
		                    },
							"GlossSee": "markup"
		                }
		            }
		        }
		    }
		}
	-------------------------------------------------------------------------
	Output file(1.xml):
		
		<glossary>
			
			<GlossDiv>
				
				<GlossList>
					
					<GlossEntry>
						
						<GlossDef>
							
							<GlossSeeAlso>
								GML
							</GlossSeeAlso>
							<GlossSeeAlso>
								XML
							</GlossSeeAlso>
							<para>
								A meta-markup language, used to create markup languages such as DocBook.
							</para>
						</GlossDef>
						<GlossSee>
							markup
						</GlossSee>
						<Acronym>
							SGML
						</Acronym>
						<GlossTerm>
							Standard Generalized Markup Language
						</GlossTerm>
						<Abbrev>
							ISO 8879:1986
						</Abbrev>
						<SortAs>
							SGML
						</SortAs>
						<ID>
							SGML
						</ID>
					</GlossEntry>
				</GlossList>
				<title>
					S
				</title>
			</GlossDiv>
			<title>
				example glossary
			</title>
		</glossary>
