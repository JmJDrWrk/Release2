function returnIndex(){
    window.location.href = "index.html";
}



//CONCLUSION FUNC

//Load RighMenus fun

function hideClass (elements) {
    elements = elements.length ? elements : [elements];
    for (var index = 0; index < elements.length; index++) {
        
        elements[index].style.visibility = 'hidden';
        elements[index].style.display = 'none';
    }
}


function loadRighMenus(elements, idName){

    console.log("ELEMENTS: " + elements)
    console.log("ID: " + idName)


    //Set visibility of all hidden and not displayed
    elements = elements.length ? elements : [elements];
    for (var index = 0; index < elements.length; index++) {

        // try{
        //    elements[index].style.visibility = 'hidden'; 
        // }catch(e){
        //     console.log(e)
        // }

        // try{
        //    elements[index].style.display = 'none'; 
        // }catch(e){
        //     console.log(e)
        // }

        try{
            hide(document.querySelectorAll(elements));
            console.log("Elementos hideados con éxito: " + document.querySelectorAll(elements))
        }catch(e){
            console.log("Error hiding elements");
            console.log(e);
        }
       
    }

    //Set display and visibility only for idName elements
    
    document.getElementById(idName).style.display = "inherit";
    document.getElementById(idName).style.visibility = "visible";
}






function deployComboBox(elements){
    var x = document.getElementsByid(elements);
    x.style.display = 'inherit';
    // console.log("Showing " + elements + " elements")
    // elements = elements.length ? elements : [elements];
    // for (var index = 0; index < elements.length; index++) {
    //   //elements[index].style.visibility = 'visible';
    //   elements[index].style.display = 'inherit';
    // }
}
function hide (elements) {
    elements = elements.length ? elements : [elements];
    for (var index = 0; index < elements.length; index++) {
        elements[index].style.visibility = 'hidden';
        elements[index].style.display = 'none';
    }
  }
function show (elements) {
    console.log("Showing " + elements + " elements")
    elements = elements.length ? elements : [elements];
    for (var index = 0; index < elements.length; index++) {
      elements[index].style.visibility = 'visible';
      elements[index].style.display = 'inherit';
    }
  }
function switchHTML(n) {
    /*var x = document.getElementsByClassName(n);*/
    /*console.log("x: " + x)*/
    console.log("Argument: " + n)
    if (n == 'servicios'){
        console.log("Servicios clicked")
        //hide(document.querySelectorAll('.right_menu_pantalla')); 
        //show(document.querySelectorAll('.right_menu_servicios')); 
        document.getElementById("id_services").style.visibility = "visible";
        document.getElementById("id_services").style.display = "inherit";
    }
    if (n == 'sonido'){
        console.log("Sonido clicked")
        hide(document.querySelectorAll('.right_menu_servicios')); 
        show(document.querySelectorAll('.right_menu_pantalla')); 
    }
    // if (x.style.display === "none") {
    //   x.style.display = "block";
    //   console.log(n + " was none and now is block")
    // } else {
    //   x.style.display = "none";
    //   console.log(n + " was block and now is none")
    // }
  }
function salute(n){
    if(n == "Sistema"){
        console.log("Sistema was clicked")
        window.location.href = "System.html";
    }else if(n == "Sistema&^Pantalla"){
        window.location.href = "SystemPantalla.html";
    }
}
// let list = document.querySelector('.list'),
// 	of = Number(window.getComputedStyle(list.querySelector('.list__item')).backgroundSize.split(' ')[0].replace(/\D+/gim, '')) / 2 || 0;
// console.info(of);

// document.addEventListener('mousemove', function(e) {
//   list.style.cssText = `--bgp-x: ${e.clientX-of}px; --bgp-y: ${e.clientY-of}px;`;
// })

//USING Eel
        
eel.expose(js_random);
function js_random() {
    return Math.random();
}

eel.expose(js_with_error);
function js_with_error() {
    var test = 0;
    test.something("does not exist");
}

function print_num(n) {
    console.log('Got this from Python: ' + n);
}

// Call Python function, and pass explicit callback function
eel.py_random()(print_num);

// Do the same with an inline callback
eel.py_random()(n => console.log('Got this from Python: ' + n));

// show usage with promises
// show no error
eel.py_exception(false)().then((result) => {
        // this will execute since we said no error
        console.log("No Error")
    }).catch((result) => {
        console.log("This won't be seen if no error")
    }
);
// show if an error occurrs
eel.py_exception(true)().then((result) => {
        // this will not execute
        console.log("No Error")
    }).catch((result) => {
        console.log("This is the repr(e) for an exception " + result.errorText);
        console.log("This is the full traceback:\n" + result.errorTraceback);
    }
)