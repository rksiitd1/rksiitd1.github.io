function generateTables() {
    const tableA = document.getElementById("tableA").value;
    const tableB = document.getElementById("tableB").value;
    const unionFileName = document.getElementById("unionFileName").value;
    const differenceFileName = document.getElementById("differenceFileName").value;

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/generate-tables", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            const response = JSON.parse(xhr.responseText);
            document.getElementById("outputMessage").innerText = response.message;
        }
    };

    xhr.send(JSON.stringify({ tableA, tableB, unionFileName, differenceFileName }));
}
