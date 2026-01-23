


    let pression1 = false;
    let corps = document.querySelector(".corps")
    let titre = document.querySelector(".t2");
    console.log(titre.value);
    

    let titre1 = document.querySelector(".t1");
    titre1.addEventListener("mouseover", function(){
        pression1 = true
        if(pression1 == true){
        titre1.style.color = "white"
        //titre1.style.fontSize = 
        }
    });
    titre1.addEventListener("mouseout", function(){
        pression1 = false
        if(pression1 == false){
        titre1.style.color = "red"
        }
    });
     
    let pression = false

    let bouton = document.getElementById("btn");
    bouton.addEventListener("click", function(){
        if(pression == false)
        {titre.style.color = "blue";
         bouton.value = "BLEU"
         corps.style.background = "green"
         pression = true;
        }
        else {
            titre.style.color = "red";
            bouton.value = "ROUGE"
            pression = false;
            corps.style.background = "cyan"
        });
