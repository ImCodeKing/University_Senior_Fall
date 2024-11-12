def generate_xml_polygons(polygons):
    xml_content = ''
    for i, poly in enumerate(polygons, start=1):
        xml_content += f'<polyin_{i}>\n'
        xml_content += f'  <points>\n'
        x_coords = poly['points'].split(';')[0]
        y_coords = poly['points'].split(';')[1]
        x_coords = [float(coord) for coord in x_coords.split(',')]
        y_coords = [float(coord) for coord in y_coords.split(',')]
        for x, y in zip(x_coords, y_coords):
            xml_content += f'              <point>{x} {y} 0</point>\n'
        xml_content += f'  </points>\n'
        xml_content += f'</polyin_{i}>\n\n'
    return xml_content

polygons = [
    {'points': '1,1,5,5;5,6,6,5'},
    {'points': '20,20,11,11,21,21;1,8,8,9,9,1'},
    {'points': '8,8,9,9;42,49,49,42'},
    {'points': '16,16,10,10,16,16,17,17,23,23,17,17;28,34,34,35,35,41,41,35,35,34,34,28'},
    {'points': '37,36,36,30,30,36,36,37;4,4,8,8,9,9,13,13'},
    {'points': '49,42,42,43,43,49;13,13,19,19,14,14'},
    {'points': '49,44,44,49;43,43,44,44'},
    {'points': '33,20,20,26,26,20,20,27,27,33;16,16,17,17,23,23,24,24,17,17'},
    {'points': '41,32,32,33,33,40,40,41;32,32,38,38,33,33,38,38'},
    {'points': '36,36,37,37;43,49,49,43'},
    {'points': '1,0,0,50,50,1;0,0,50,50,49,49'},
    {'points': '50,1,1,49,49,50;0,0,1,1,49,49'},
    {'points': '1,1,9,9,10,10,9,9;20,21,21,27,27,14,14,20'},
    {'points': '23,22,22,23,23,29,29,23;40,40,45,45,43,43,42,42'},
    {'points': '33,32,32,40,40,33;22,22,28,28,27,27'},
    {'points': '25,25,26,26;27,32,32,27'}
]

xml_text = generate_xml_polygons(polygons)
print(xml_text)