filename = "input.txt"
with open('somefile.txt', 'w') as output:
    with open(filename) as f:
        for line in f:
            array = line.split('|')
            MappingType, LayerID, ProductID, LoginID, ContactKey, OrderNo, Token = array[1].strip(),array[2].strip(),array[3].strip(),array[4].strip(),array[5].strip(),array[6].strip(),array[7].strip()
            output.write('\n\n')
            output.write("@Order:" + OrderNo + " @User:" + LoginID + "\n")
            output.write("Scenario: Record Royalty info for  " + MappingType + "\n")
            output.write("Given The map layers panel has loaded\n")
            output.write("And I have the " + MappingType + " (" + LayerID + ") layer not selected\n")
            output.write("When I select the " + MappingType + " (" + LayerID + ") layer\n")
            output.write("Then a royalty is recorded with an ID of \"" + OrderNo + "-" + LayerID + "\"\n")
            output.write("And the royalty record \"" + OrderNo + "-" + LayerID + "\" has UserId of " + ContactKey + "\n")
            output.write("And the royalty record \"" + OrderNo + "-" + LayerID + "\" has ProductId of " + ProductID + "\n")
            output.write("And the royalty record \"" + OrderNo + "-" + LayerID + "\" has Token of " + Token + "\n")
            output.write("And the royalty record \"" + OrderNo + "-" + LayerID + "\" has AppName of ecAnalysis\n")
            output.write("And the royalty record \"" + OrderNo + "-" + LayerID + "\" has WktGeometry of the extent reported by the OpenLayers map control\n")
            output.write("And the royalty record \"" + OrderNo + "-" + LayerID + "\" has SessionId of the Landmark login cookie value\n")

input()

