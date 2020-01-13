
var listMessages = [
        {
            author: "GrandPy",
            message: "Bonjour, je suis PaPy BoT, puis-je te renseigner sur lieu en particulier ?"
        },
        {
            author: "User",
            message: "Bonjour GrandPy ! Tu connais openclassroom ?"
        },
        {
            author: "GrandPy",
            message: "La bonne blague !"
        }
    ]
let myParser new Parser("GrandPy", "Bonjour, je suis PaPy BoT, puis-je te renseigner sur lieu en particulier ?")


for (var i = 0; i < listMessages.length; i++) {

    var pElt = document.createElement("p");
    pElt.style.width = ("100%");
    //pElt.className = "lien";
    var messageElt = document.createElement("a");
    if (listMessages[i]["author"] == "User"){
        pElt.style.textAlign  = ("Right");
    }
    messageElt.textContent = listMessages[i]["message"];
    var brElt = document.createElement("br");

    var spanElt = document.createElement("span");
    var auteurElt = document.createElement("a");
    auteurElt.textContent = "Ajouté par "+listMessages[i]["author"];

    pElt.appendChild(messageElt);
    pElt.appendChild(brElt);
    pElt.appendChild(auteurElt);

    document.getElementById("echange").appendChild(pElt);

}