var text = "{{Hello|Hi|Hola}, How {have you been|are you doing}? " +
           "Take care. {{Thanks and|Best} Regards|Cheers|Thanks}";

var matches, options, random;

var regEx = new RegExp(/{([^{}]+?)}/);

while((matches = regEx.exec(text)) !== null) {
  options = matches[1].split("|");
  random = Math.floor(Math.random() * options.length);
  text = text.replace(matches[0], options[random]);
}

console.log(text);