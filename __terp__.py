{
    "name":"Quotation Report Module ",
    "description" : "Create the quortation report for user",
    "version":"1.0",
     "author" : "chanmyay",
    "category" : "Generic Modules/Sale",
    "website":"http://www.vectorinfotech.com",
    "depends":[
        "base",
        "sale",
        "account",
        "product",
      
    ],
    "demo_xml":[],
    "update_xml":[
  
	"security/service_security.xml",
 	"security/ir.model.access.csv", 
        "sale_field.xml",
             
    ],
    "active": False,
    "installable": True,
    
}
