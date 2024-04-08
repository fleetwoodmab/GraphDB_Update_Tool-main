document.querySelector("button").onclick = function () {   
    var graph = document.getElementById("graphs").value;
    eel.update_graph(graph)();
    document.getElementById("placeholder").innerHTML = "Updated!";
}
