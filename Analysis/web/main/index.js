function $(e){
    return document.querySelectorAll(e)
}

function ex_form(){
    for (let i = 0; i < $('.radio').length;i++){
        console.log(i)
        $(".radio")[i].addEventListener("click", function(){
            for(let x = 0; x < $('.radio').length; x++){
                if (i != x){
                    $(".form")[x].style.visibility = "hidden";
                }else{
                    $(".form")[x].style.visibility = "visible";
                }
            }
        })
    }
}

ex_form()
