# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals

import json
import frappe
from frappe.model.naming import make_autoname

def naming_series_for_item(doc, method):
    item_group = doc.item_group
    # Raw Materials
    if item_group == "water":
	    doc.item_code = make_autoname('0201-.####')
    elif item_group == "Mineral":
	    doc.item_code = make_autoname('0202-.####')
    # Packaging
    elif item_group == "Preform":
	    doc.item_code = make_autoname('0301-.####')
    elif item_group == "Cap":
	    doc.item_code = make_autoname('0302-.####')
    elif item_group == "Labels":
	    doc.item_code = make_autoname('0303-.####')
    elif item_group == "Carton":
	    doc.item_code = make_autoname('0304-.####')
    elif item_group == "Shrink":
	    doc.item_code = make_autoname('0305-.####')
    elif item_group == "Shrink with Pad":
	    doc.item_code = make_autoname('0306-.####')
    elif item_group == "Shrink withTray":
	    doc.item_code = make_autoname('0307-.####')
    elif item_group == "Pallet":
	    doc.item_code = make_autoname('0308-.####')
    elif item_group == "Stretch film":
	    doc.item_code = make_autoname('0309-.####')
    elif item_group == "Glue":
	    doc.item_code = make_autoname('0310-.####')
    #Chemicals
    elif item_group == "INORGANIC":
        doc.item_code = make_autoname('0401-.####')
    elif item_group == "RESEARCH CHEMICALS":
        doc.item_code = make_autoname('0402-.####')
    #Chemical Detergents and Sterilizers
    elif item_group == "Equipment":
        doc.item_code = make_autoname('0501-.####')
    elif item_group == "plant":
        doc.item_code = make_autoname('0502-.####')
    elif item_group == "Personal":
        doc.item_code = make_autoname('0503-.####')
    #Spare parts, filters and oils
    elif item_group == "machinery":
        doc.item_code = make_autoname('0601-.####')
    elif item_group == "Cars":
        doc.item_code = make_autoname('0602-.####')
    #Uniform and shoes
    elif item_group == "Shirt":
        doc.item_code = make_autoname('0701-.####')
    elif item_group == "scrub":
        doc.item_code = make_autoname('0702-.####')
    elif item_group == "PANT":
        doc.item_code = make_autoname('0703-.####')
    elif item_group == "shoes":
        doc.item_code = make_autoname('0704-.####')
    #Libraries and publications
    elif item_group == "NCR Invoice":
        doc.item_code = make_autoname('0801-.####')
    elif item_group == "Letterheads":
        doc.item_code = make_autoname('0802-.####')
    elif item_group == "Business Cards":
        doc.item_code = make_autoname('0803-.####')
    elif item_group == "Office Supplies":
        doc.item_code = make_autoname('0804-.####')
    #Computers and software
    elif item_group == "Computers":
        doc.item_code = make_autoname('0901-.####')
    elif item_group == "software":
        doc.item_code = make_autoname('0902-.####')
    elif item_group == "Central":
        doc.item_code = make_autoname('0903-.####')
    elif item_group == "server Rack":
        doc.item_code = make_autoname('0904-.####')
    elif item_group == "security cameras":
        doc.item_code = make_autoname('0905-.####')
    #Furniture and fittings
    elif item_group == "plant":
        doc.item_code = make_autoname('1001-.####')
    elif item_group == "Offices":
        doc.item_code = make_autoname('1001-.####')
    elif item_group == "Laboratories":
        doc.item_code = make_autoname('1001-.####')
    elif item_group == "house":
        doc.item_code = make_autoname('1001-.####')
    #Industrial equipment and instruments
    elif item_group == "Coolers":
        doc.item_code = make_autoname('1101-.####')
    elif item_group == "Pneumatic pump":
        doc.item_code = make_autoname('1102-.####')
    elif item_group == "Inkjet Printer":
        doc.item_code = make_autoname('1103-.####')
    elif item_group == "blow mould":
        doc.item_code = make_autoname('1104-.####')
    #Laboratory equipment and materials
    elif item_group == "LAB EQUIPMENT":
        doc.item_code = make_autoname('1201-.####')
    elif item_group == "LAB INSTRUMENTS":
        doc.item_code = make_autoname('1202-.####')
    elif item_group == "REAGENTS & STANDARDS":
        doc.item_code = make_autoname('1203-.####')
    #Services	
    elif item_group == "Transportation":
        doc.item_code = make_autoname('1301-.####')
    elif item_group == "Customs Clearance":
        doc.item_code = make_autoname('1302-.####')
    elif item_group == "Pest Control":
        doc.item_code = make_autoname('1303-.####')
    elif item_group == "Transalation":
        doc.item_code = make_autoname('1304-.####')
    elif item_group == "Hire workers":
        doc.item_code = make_autoname('1305-.####')
    elif item_group == "Swage Water":
        doc.item_code = make_autoname('1306-.####')
    #electric machines	
    elif item_group == "Refrigerators":
        doc.item_code = make_autoname('1401-.####')
    elif item_group == "Air conditioners":
        doc.item_code = make_autoname('1402-.####')
    elif item_group == "cookers":
        doc.item_code = make_autoname('1403-.####')
    elif item_group == "Dryers":
        doc.item_code = make_autoname('1404-.####')
    elif item_group == "washers":
        doc.item_code = make_autoname('1405-.####')
    elif item_group == "Screen TV's":
        doc.item_code = make_autoname('1406-.####')
    #safety tools	    
    elif item_group == "Fire extinguishing systems":
        doc.item_code = make_autoname('1501-.####')
    elif item_group == "Equipment for fire-fighting":
        doc.item_code = make_autoname('1502-.####')
    elif item_group == "Alarm systems":
        doc.item_code = make_autoname('1503-.####')
    elif item_group == "Fireproof materials":
        doc.item_code = make_autoname('1504-.####')
    #Industrial printer inks	
    elif item_group == "inks":
        doc.item_code = make_autoname('1601-.####')
    elif item_group == "Washing Solution":
        doc.item_code = make_autoname('1602-.####')
    #Devices and tools	
    elif item_group == "Hand Trolley":
        doc.item_code = make_autoname('1701-.####')
    elif item_group == "tools":
        doc.item_code = make_autoname('1702-.####')
    elif item_group == "WELDING  ELECTRODE":
        doc.item_code = make_autoname('1703-.####')
    #Hygiene and sterilization	
    elif item_group == "Waste Bin":
        doc.item_code = make_autoname('1801-.####')
    elif item_group == "safety tools":
        doc.item_code = make_autoname('1802-.####')
    elif item_group == "Liquid Soap":
        doc.item_code = make_autoname('1803-.####')
    elif item_group == "cleaning tools":
        doc.item_code = make_autoname('1804-.####')
    elif item_group == "Trash Bags":
        doc.item_code = make_autoname('1805-.####')
    elif item_group == "Cleaning paper":
        doc.item_code = make_autoname('1806-.####')
    elif item_group == "Sanitary materials":
        doc.item_code = make_autoname('1807-.####')
    elif item_group == "Sterilizer":
        doc.item_code = make_autoname('1808-.####')
    elif item_group == "insect traps":
        doc.item_code = make_autoname('1809-.####')
    elif item_group == "Glue Board":
        doc.item_code = make_autoname('1810-.####')
    #Scraps 	
    elif item_group == "Plastic products":
        doc.item_code = make_autoname('1901-.####')
    elif item_group == "Cartons":
        doc.item_code = make_autoname('1902-.####')
    elif item_group == "Pallets":
        doc.item_code = make_autoname('1903-.####')
    #Marketing and exhibitions	
    elif item_group == "Marketing campaigns":
        doc.item_code = make_autoname('2001-.####')
    elif item_group == "Visual production":
        doc.item_code = make_autoname('2002-.####')
    elif item_group == "Digital Marketing":
        doc.item_code = make_autoname('2003-.####')
    elif item_group == "Creative Design":
        doc.item_code = make_autoname('2004-.####')
    elif item_group == "Advertisement Boards":
        doc.item_code = make_autoname('2005-.####')

