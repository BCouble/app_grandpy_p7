class Converse{
    constructor(author, message){
        this.author = author;
        this.message = message;
    }
    getConserve(){
        return this.author+" "+this.message;
    }
    getCreateDom(){
        return createDom();
    }
    conserve(){
        console.log(this.author+" "+this.message)
    }
    createDom(){
        var pElt = document.createElement("p");
        pElt.style.width = ("100%");
        pElt.style.backgroundColor = ("#CC34FE");
        //pElt.className = "lien";
        var messageElt = document.createElement("a");

        messageElt.textContent = this.message;
        var brElt = document.createElement("br");
        var spanElt = document.createElement("span");
        var auteurElt = document.createElement("a");
        auteurElt.textContent = "Ajouté par "+this.author;

        pElt.appendChild(messageElt);
        pElt.appendChild(brElt);
        pElt.appendChild(auteurElt);

        document.getElementById("echange").appendChild(pElt);
    }
    configMe(){
        //if (this.author == "GrandPy"){
        position = "left";
        color = "#CC34EF";
        //}else if (this.author == "User"){
        //    position = "right";
        //    color = "#CC43FE";
        //}
        pElt.style.textAlign  = (position);

    }
}


var author = "GrandPy";
var message = "Bonjour, je suis PaPy BoT, puis-je te renseigner sur lieu en particulier ?";
const mess = new Converse(author, message);

mess.createDom();
console.log(mess.conserve());