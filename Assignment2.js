function generateTable() {
  const rows = document.getElementById("rows").value;
  const columns = document.getElementById("columns").value;

  // Clear previous table if any
  const tableContainer = document.getElementById("tableContainer");
  tableContainer.innerHTML = "";

  // Create the table
  const table = document.createElement("table");

  // Create the table rows and columns dynamically
  for (let i = 0; i < rows; i++) {
    const row = document.createElement("tr");

    for (let j = 0; j < columns; j++) {
      const cell = document.createElement("td");

      // Create input fields inside each cell
      const inputField = document.createElement("input");
      inputField.type = "text";
      inputField.placeholder = `Row ${i + 1}, Col ${j + 1}`;
      cell.appendChild(inputField);

      row.appendChild(cell);
    }
    table.appendChild(row);
  }

  tableContainer.appendChild(table);
}

function submitForm() {
  const table = document.querySelector("table");

  if (!table) {
    alert("Please generate a table first.");
    return;
  }

  const inputs = table.querySelectorAll("input");
  let allFilled = true;

  // Check if any input field is empty
  inputs.forEach((input) => {
    if (input.value.trim() === "") {
      allFilled = false;
    }
  });

  if (allFilled) {
    alert("Form submitted successfully!");
  } else {
    alert("Please fill in all the fields before submitting.");
  }
}
