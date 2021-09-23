import * as CoinMarket from '/coins/coinmarket_js';


function CreatingTable(data) {
    var table = document.getElementById('table');
    // declaring the COLUMS titles //
    var title_line = document.createElement('tr');
    var title_css = document.createElement('thead');
    var query2 = CoinMarket.CoinObject(data[0]);
    var add_obj_th = document.createElement('th');
    add_obj_th.innerHTML = "Adicionar investimento"
    title_line.append(add_obj_th);

    Object.entries(query2).forEach((key) => {
        let title_cel = document.createElement('th');
        title_cel.id = 'title_' + key[0];
        let title_cel_value = document.createTextNode(key[0]);
        title_cel.appendChild(title_cel_value);
        title_line.appendChild(title_cel);
        // ON/OFF Filter
        var form = document.getElementById('form');
        var label = document.createElement('label');
        label.id = 'label_' + key[0];
        label.htmlFor = 'input_' + key[0];
        label.innerHTML = key[0];
        label.style.marginLeft = '10px'
        label.style.backgroundColor = 'green';
        var input = document.createElement('input');
        input.type = 'checkbox';
        input.hidden = true;
        input.id = 'input_' + key[0];
        form.appendChild(label);
        form.appendChild(input);
        input.addEventListener("change", () => { HideColumn(key[0]) })
        // FORM END
    });
    title_css.appendChild(title_line);
    table.appendChild(title_css);
    SearchBar(data)
}


function SearchBar(data) {
    var form = document.getElementById('searching');
    var bar = document.createElement('input');
    form.appendChild(bar);
    var filteredList = data
    bar.addEventListener('keyup', (e) => {
        let searchText = e.target.value;
        let filteredList = data.filter((coin) => {
            return coin.name.includes(searchText) || coin.symbol.includes(searchText);
        });
        UpdatingSearch(filteredList)
    });
    return CreatingData(filteredList)
};


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// function CSRFInputPass(form) {
//     let csrf = document.createElement("input")
//     csrf.type = "hidden"
//     csrf.name = "csrfmiddlewaretoken"
//     csrf.value = getCookie('csrftoken')
//     return form.appendChild(csrf)
// }


function PostForm(obj) {
    let cel = document.createElement('td')
    let payd = document.createElement('input')
    let ammount = document.createElement('input')
    let submit = document.createElement('button')
    submit.innerHTML = "Enviar"
    payd.placeholder = "Valor da Moeda"
    ammount.placeholder = "Quantidade em Dollar"

    submit.addEventListener('click', () => {
        var requestin = new XMLHttpRequest()
        requestin.open("POST", "/coins/home/")
        var form = { payd: payd.value, ammount: ammount.value }
        var data = JSON.stringify({ ...form, ...obj })
        requestin.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
        console.log(getCookie('csrftoken'))
        requestin.setRequestHeader("Content-Type", "application/json")
        requestin.send(data)
        alert("okss")
    })
    cel.appendChild(payd)
    cel.appendChild(ammount)
    cel.appendChild(submit)
    return cel
}



function CreatingData(data) {
    var ones = data
    let cel_css = document.createElement('tbody');
    cel_css.id = 'table_body';
    for (let o of ones.slice(0, 100)) {
        var line = document.createElement("tr");
        //PARTICULARIDADE DO COINMARKET //
        var new_obj = CoinMarket.CoinObject(o);
        line.append(PostForm(o))
        for (var i in new_obj) {
            var cel = document.createElement("td");
            cel.style.display = 'table-cell';
            cel.className = 'cel_' + i;
            var result = document.createTextNode(new_obj[i]);
            cel.appendChild(result);
            line.appendChild(cel);
        };
        cel_css.appendChild(line);
        table.appendChild(cel_css);
    }
}


function UpdatingSearch(data) {
    var table_body = document.getElementById('table_body');
    table_body.parentNode.removeChild(table_body)
    CreatingData(data)
}

function HideColumn(c) {
    var elements = document.getElementsByClassName('cel_' + c);
    var title = document.getElementById('title_' + c);
    var check = document.getElementById('label_' + c);
    var input = document.getElementById('input_' + c);

    if (input.checked != true) {
        title.style.display = 'none';
        check.style.backgroundColor = 'red';
        Array.from(elements).map((e) => { e.style.display = 'none' })
    }
    else {
        title.style.display = 'table-cell'
        check.style.backgroundColor = 'green'
        Array.from(elements).map((e) => { e.style.display = 'table-cell' })
    };

};

function Updating() {
    setInterval(() => {
        var table_body = document.getElementById('table_body');
        // "{% url 'restart' %}"
        fetch("{% url 'restart' %} ")
            .then(response => response.json())
            .then(json => CreatingData(json['data']))
            .then(table_body.parentNode.removeChild(table_body))
    }, 782000);
};



// "{% url 'restart' %}"
await fetch("{% url 'restart' %}")
    .then(response => response.json())
    .then(json => CreatingTable(json['data']));
document.addEventListener('DOMContentLoaded', function () { Updating() });


