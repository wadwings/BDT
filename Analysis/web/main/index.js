function $(e){
    return document.querySelectorAll(e)
}

function ex_form(){
    const xmlhttp = new XMLHttpRequest()
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
        $(".submit")[i].addEventListener("click", function(){
            $('#f_bc')[0].style.transform = "scale(0.8) translate(-150%, -50%)";
            $('#f_bc')[0].style.transition = "0.5s";
            $('#bc1')[0].style.left = "27%";
            $('#bc2')[0].style.right = "20%";
            $('#img_div')[0].style.opacity = 1;
            xmlhttp.open("POST", "/server.js", true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset = utf-8");
            if (i === 0)    {xmlhttp.send(encodeURI("city=" + $("#city")[0].value + '&option=month_tem&year=' + $(".year")[0].value + '&month=' + $('.month')[0].value + '&mode=' + $('.mode')[0].value));  pic_push(encodeURI('./pic/' + $("#city")[0].value + '-' + $(".year")[0].value + '-' + $('.month')[0].value + '-' + $('.mode')[0].value) + '.png');}
            else if(i === 1)    {xmlhttp.send(encodeURI("city=" + $("#city")[0].value + '&option=year_tem&year=' + $(".year")[1].value + '&mode=' + $('.mode')[1].value));  pic_push(encodeURI('./pic/' + $("#city")[0].value + '-' + $(".year")[1].value + '-' + $('.mode')[1].value) + '.png');}
            else if(i === 2)    {xmlhttp.send(encodeURI("city=" + $("#city")[0].value + '&option=month_tem_ch&month=' + $('.month')[1].value + '&mode=' + $('.mode')[2].value));    pic_push(encodeURI('./pic/' + $("#city")[0].value + '-' + $('.month')[1].value + '-' + $('.mode')[2].value) + '.png');}
        })
    }
}

let pic_list = ["./pic/vacant.png","./pic/vacant.png","./pic/vacant.png","./pic/vacant.png"]
function pic_push(str){
    setTimeout(function(){
        for(let x = 4; x > 0; x--)
            pic_list[x] = pic_list[x - 1]
        pic_list[0] = str
        apply_pic()
    }, 6000)
}

function apply_pic(){
    for(let x = 0; x < 4; x++){
        $('.img')[x].src = pic_list[x];
    }
}

function ex_pic(){
    for(let i = 1; i < 4; i++)
        $('.img')[i].addEventListener('click', function(){
            tmp = pic_list[i];
            pic_list[i] = pic_list[0];
            pic_list[0] = tmp;
            apply_pic();
    })
}

function init(){
    document.querySelector('#bc1').style.height = window.screen.height + 'px'
    document.querySelector('#bc2').style.height = window.screen.height + 'px'
}

init()
ex_form()
apply_pic()
ex_pic()