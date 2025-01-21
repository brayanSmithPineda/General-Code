module.exports = function(htmlTemplate, productsArray1) {
    let output = htmlTemplate.replace("{{%NAME%}}", productsArray1.name);
    output = output.replace("{{%MODELNAME%}}", productsArray1.modeName);
    output = output.replace("{{%MODELNO%}}", productsArray1.modelNumber);
    output = output.replace("{{%SIZE%}}", productsArray1.size);
    output = output.replace("{{%CAMERA%}}", productsArray1.camera);
    output = output.replace("{{%PRICE%}}", productsArray1.price);
    output = output.replace("{{%COLOR%}}", productsArray1.color);
    output = output.replace("{{%ID%}}", productsArray1.id);
    output = output.replace("{{%ROM%}}", productsArray1.ROM);
    output = output.replace("{{%DESC%}}", productsArray1.Description);
  
    return output;
  };