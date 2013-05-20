window.onload = function(){
    var o=document.getElementById("s");
    var t="其实搜索很简单^_^";
    o.onblur = function(){
        if(o.value==""){
            o.value=t;
        }
    }
    o.onfocus = function(){
        if(o.value==t){
            o.value="";
        }
    }
    o.onblur();
}
