#  TranslateApi

 **This uses the openAPI gpt-3 api.**

**Usage : make an api call to the endpoint "https://jbotrex.pythonanywhere.com/translate" and follow the format below:**

**what is needed from you are:**

+ the data to be translated and 
+ the language.

 
   
 
    async function translate(){
    let data= data
    let language=language
    let response
    let translated
    response=await fetch("/translate",{method:"POST",headers: { "Content-type": "application/json" },
    body: JSON.stringify({"data":data,"language":language})})
    translated=await response.text()
    console.log(translated)
    }
