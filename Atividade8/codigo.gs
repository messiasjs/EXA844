function doGet(request){
  if (request.parameter.author!= null && request.parameter.message != null){
      SpreadsheetApp.getActive().getSheetByName('Messages').appendRow([request.parameter.message, request.parameter.author, new Date()]);
  }
  var template = HtmlService.createTemplateFromFile('Messages');
  return template.evaluate();
}


function getMessages(){
  var ms = SpreadsheetApp.getActive().getSheetByName('Messages');
  var data = ms.getRange(2,1,ms.getLastRow()-1,3).getValues();
  return JSON.stringify(data);
}
