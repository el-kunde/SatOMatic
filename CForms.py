class FormLogin:
	userInputId = "Ecom_User_ID"
	passInputId = "Ecom_Password"
	
class FormReceptor:
	rfcInputId 		= "cfdi:Receptor_@rfc"
	nombreInputId 	= "cfdi:Receptor_@nombre"
	
	domicilioCheckboxId = "IsEnabledDomicilio"
	
	calleInputId 		= "cfdi:Receptor_cfdi:Domicilio_@calle"
	numExtInputId 		= "cfdi:Receptor_cfdi:Domicilio_@noExterior"
	numIntInputId		= "cfdi:Receptor_cfdi:Domicilio_@noInterior"
	coloniaInputId		= "cfdi:Receptor_cfdi:Domicilio_@colonia"
	localidadInputId	= "cfdi:Receptor_cfdi:Domicilio_@localidad"
	referenciaInputId	= "cfdi:Receptor_cfdi:Domicilio_@referencia"
	municipioInputId	= "cfdi:Receptor_cfdi:Domicilio_@municipio"
	paisInputId			= "cfdi:Receptor_cfdi:Domicilio_@pais"
	estadoSelectId		= "cfdi:Receptor_cfdi:Domicilio_@estado"
	cpInputId			= "cfdi:Receptor_cfdi:Domicilio_@codigoPostal"
	nextButtonValue		= "Siguiente"

class FormComprobante:
	serieInputId		= "cfdi:Comprobante_@serie"
	folioInputId		= "cfdi:Comprobante_@folio"
	lugarInputId		= "cfdi:Comprobante_@LugarExpedicion"
	comprobanteSelectId	= "cfdi:Comprobante_@tipoDeComprobante"
	monedaInputId		= "cfdi:Comprobante_@Moneda"
	cambioInputId		= "cfdi:Comprobante_@TipoCambio"
	formaPagoInputId	= "cfdi:Comprobante_@formaDePago"
	metodoPagoInputId	= "cfdi:Comprobante_@metodoDePago"
	cuentaPagoInputId	= "cfdi:Comprobante_@NumCtaPago"
	condPagoInputId		= "cfdi:Comprobante_@condicionesDePago"
	
	cantidadInputId		= "ItemConcepto_Cantidad"
	unidadInputId		= "ItemConcepto_Unidad"
	numIdentInputId		= "ItemConcepto_NoId"
	descripcionInputId	= "ItemConcepto_Descripcion"
	valorUnitInputId	= "ItemConcepto_PrecioUnitario"
	addConceptButtonId	= "btnAddConcepto"
	
	impTrasCheckboxId	= "IsEnabledImpuestoTrasladado"
	
	impTrasSelectId		= "ItemTraslado_Impuesto"
	impTrasTasaInputId	= "ItemTraslado_Tasa"
	impTrasImpInputId	= "ItemTraslado_Importe"
	addImpTrasButtonId	= "btnTrasladado"
	
	impRetCheckboxId	= "IsEnabledImpuestoRetenido"
	
	impRetSelectId		= "ItemRetencion_Impuesto"
	impRetImpInputId	= "ItemRetencion_Importe"
	addImpRetButtonId	= "btnRetencion"