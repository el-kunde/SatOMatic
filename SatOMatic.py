import getpass
import json
from CForms import FormLogin as FL
from CForms import FormReceptor as FR
from CForms import FormComprobante as FC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class UserLoginInfo:	
	def __init__(self,usrLogin,usrPass):
		self.username = usrLogin
		self.password = usrPass
	
def getUserLoginInfo():
	username = input(" RFC: ")
	password = getpass.getpass("FIEL: ")
	return UserLoginInfo(username,password)	
		
if __name__ == "__main__":
	
	# Prompt user to enter credentials
	userLoginInfo = getUserLoginInfo()
	
	# Load Firefox and login page
	Firefox = webdriver.Firefox()
	Firefox.get('https://cfdiau.sat.gob.mx/nidp/app/login?id=SATUPCFDiCon&sid=0&option=credential')
	
	#Enter user credentials on login page
	userInputId = Firefox.find_element_by_name(FL.userInputId)
	passInputId = Firefox.find_element_by_name(FL.passInputId)
	submitButton = Firefox.find_element_by_id('submit')
	userInputId.send_keys(userLoginInfo.username)	
	passInputId.send_keys(userLoginInfo.password)
	submitButton.send_keys(Keys.RETURN)
	
	# Load CFDI page
	Firefox.get('https://pacsat.facturaelectronica.sat.gob.mx/cfdi/generacioncfdi')
	
	# Click on "RECEPTOR" tab. This may fail due loading times
	# To be fixed in another version
	receptorTab = Firefox.find_element_by_xpath("//li[@onclick='goToReceptor()']")
	receptorTab.click()
	
	# Open data file
	myData = open("data.json")
	myData = json.load(myData)
	
	# Finding RECEPTOR FORM fields
	rfcInput 	= Firefox.find_element_by_id(FR.rfcInputId)
	nombreInput	= Firefox.find_element_by_id(FR.nombreInputId)
	
	domicilioCheckbox = Firefox.find_element_by_id(FR.domicilioCheckboxId)
	
	calleInput 			= Firefox.find_element_by_id(FR.calleInputId)
	numExtInput 		= Firefox.find_element_by_id(FR.numExtInputId)
	numIntInput			= Firefox.find_element_by_id(FR.numIntInputId)
	coloniaInput		= Firefox.find_element_by_id(FR.coloniaInputId)
	localidadInput		= Firefox.find_element_by_id(FR.localidadInputId)
	referenciaInput		= Firefox.find_element_by_id(FR.referenciaInputId)
	municipioInput		= Firefox.find_element_by_id(FR.municipioInputId)
	paisInput			= Firefox.find_element_by_id(FR.paisInputId)
	estadoSelect		= Select(Firefox.find_element_by_id(FR.estadoSelectId))
	cpInput				= Firefox.find_element_by_id(FR.cpInputId)
	toComprobanteButton	= Firefox.find_element_by_xpath("//input[@value='"+FR.nextButtonValue+"']")
	
	# Filling RECEPTOR FORM data
	rfcInput.send_keys(myData["receptor"]["rfc"])
	nombreInput.send_keys(myData["receptor"]["nombre"])
	
	domicilioCheckbox.click()
	
	calleInput.send_keys(myData["receptor"]["domicilio"]["calle"])
	numExtInput.send_keys(myData["receptor"]["domicilio"]["numExt"])
	numIntInput.send_keys(myData["receptor"]["domicilio"]["numInt"])
	coloniaInput.send_keys(myData["receptor"]["domicilio"]["colonia"])
	localidadInput.send_keys(myData["receptor"]["domicilio"]["localidad"])
	referenciaInput.send_keys(myData["receptor"]["domicilio"]["referencia"])
	municipioInput.send_keys(myData["receptor"]["domicilio"]["municipio"])
	paisInput.send_keys(myData["receptor"]["domicilio"]["pais"])
	estadoSelect.select_by_visible_text(myData["receptor"]["domicilio"]["estado"])
	cpInput.send_keys(myData["receptor"]["domicilio"]["cp"])
	toComprobanteButton.click()
	
	# Finding COMPROBANTE FORM fields
	serieInput 			= Firefox.find_element_by_id(FC.serieInputId)	
	folioInput 			= Firefox.find_element_by_id(FC.folioInputId)
	lugarInput 			= Firefox.find_element_by_id(FC.lugarInputId)
	comprobanteSelect 	= Select(Firefox.find_element_by_id(FC.comprobanteSelectId))
	monedaInput 		= Firefox.find_element_by_id(FC.monedaInputId)
	cambioInput 		= Firefox.find_element_by_id(FC.cambioInputId)
	formaPagoInput 		= Firefox.find_element_by_id(FC.formaPagoInputId)
	metodoPagoInput 	= Firefox.find_element_by_id(FC.metodoPagoInputId)
	cuentaInput 		= Firefox.find_element_by_id(FC.cuentaPagoInputId)
	condPagoInput 		= Firefox.find_element_by_id(FC.condPagoInputId)
	
	# Filling COMPROBANTE FORM data
	serieInput.send_keys(myData["comprobante"]["comprobante"]["serie"])
	folioInput.send_keys(myData["comprobante"]["comprobante"]["folio"])
	lugarInput.send_keys(myData["comprobante"]["comprobante"]["lugarDeExpedicion"])
	comprobanteSelect.select_by_visible_text(myData["comprobante"]["comprobante"]["tipoDeComprobante"])
	monedaInput.send_keys(myData["comprobante"]["comprobante"]["moneda"])
	cambioInput.send_keys(myData["comprobante"]["comprobante"]["tipoDeCambio"])
	formaPagoInput.send_keys(myData["comprobante"]["comprobante"]["formaDePago"])
	metodoPagoInput.send_keys(myData["comprobante"]["comprobante"]["metodoDePago"])
	cuentaInput.send_keys(myData["comprobante"]["comprobante"]["numCuentaDePago"])
	condPagoInput.send_keys(myData["comprobante"]["comprobante"]["condicionesDePago"])
	
	# Finding CONCEPTOS FORM fields
	cantidadInput 		= Firefox.find_element_by_id(FC.cantidadInputId)
	unidadInput 		= Firefox.find_element_by_id(FC.unidadInputId)
	numIdentInput 		= Firefox.find_element_by_id(FC.numIdentInputId)
	descripcionInput 	= Firefox.find_element_by_id(FC.descripcionInputId)
	precioInput 		= Firefox.find_element_by_id(FC.valorUnitInputId)
	addConceptInput		= Firefox.find_element_by_id(FC.addConceptButtonId)
	
	# Filling CONCEPTOS FORM data
	cantidadInput.send_keys(myData["comprobante"]["conceptos"]["cantidad"])
	unidadInput.send_keys(myData["comprobante"]["conceptos"]["unidad"])
	numIdentInput.send_keys(myData["comprobante"]["conceptos"]["numIdentificacion"])
	descripcionInput.send_keys(myData["comprobante"]["conceptos"]["descripcion"])
	precioInput.send_keys(myData["comprobante"]["conceptos"]["valorUnitario"])
	addConceptInput.click()
	
	# Finding IMPUESTOS TRASLADADOS fields
	impTrasCheckbox 	= Firefox.find_element_by_id(FC.impTrasCheckboxId)
	impTrasSelect 		= Select(Firefox.find_element_by_id(FC.impTrasSelectId))
	tasaInput 			= Firefox.find_element_by_id(FC.impTrasTasaInputId)
	importeInput 		= Firefox.find_element_by_id(FC.impTrasImpInputId)	
	addImpTrasButton 	= Firefox.find_element_by_id(FC.addImpTrasButtonId)
	
	# Filling IMPUESTOS TRASLADADOS data
	impTrasCheckbox.click()
	
	for impTras in myData["comprobante"]["impTras"]:
		impTrasSelect.select_by_visible_text(impTras["tipo"])
		tasaInput.send_keys(impTras["tasa"])
		importeInput.send_keys(impTras["importe"])
		addImpTrasButton.click()
	
	# Finding IMPUESTOS RETENIDOS fields
	impRetCheckbox 		= Firefox.find_element_by_id(FC.impRetCheckboxId)
	impRetSelect 		= Select(Firefox.find_element_by_id(FC.impRetSelectId))	
	importeInput 		= Firefox.find_element_by_id(FC.impRetImpInputId)
	addImpRetButton 	= Firefox.find_element_by_id(FC.addImpRetButtonId)
	
	# Filling IMPUESTOS RETENIDOS data
	impRetCheckbox.click()
	
	for impRet in myData["comprobante"]["impRet"]:
		impRetSelect.select_by_visible_text(impRet["tipo"])
		importeInput.send_keys(impRet["importe"])
		addImpRetButton.click()