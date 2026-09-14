const buttons = [...document.querySelectorAll('.operation')];
const form = document.querySelector('#calculator-form');
const operands = document.querySelector('#operands');
const output = document.querySelector('#result');
let selected = JSON.parse(buttons[0].dataset.operation);

function drawInputs(focusFirst = true) {
  operands.replaceChildren(...selected.operands.map((name, index) => {
    const label = document.createElement('label');
    label.textContent = name.replace('_', ' ');
    const input = document.createElement('input');
    input.type = 'number'; input.step = 'any'; input.name = name; input.required = true;
    input.autocomplete = 'off';
    label.append(input);
    if (index === 0 && focusFirst) requestAnimationFrame(() => input.focus());
    return label;
  }));
}

function choose(button, focusOperand = true) {
  buttons.forEach(item => {
    const isSelected = item === button;
    item.classList.toggle('selected', isSelected);
    item.setAttribute('aria-checked', String(isSelected));
    item.tabIndex = isSelected ? 0 : -1;
  });
  selected = JSON.parse(button.dataset.operation); drawInputs(focusOperand); output.textContent = 'Ready when you are.';
}

buttons.forEach((button, index) => {
  button.addEventListener('click', () => choose(button));
  button.addEventListener('keydown', event => {
    if (!['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp'].includes(event.key)) return;
    event.preventDefault();
    const direction = ['ArrowRight', 'ArrowDown'].includes(event.key) ? 1 : -1;
    const next = buttons[(index + direction + buttons.length) % buttons.length];
    choose(next, false); next.focus();
  });
});

form.addEventListener('submit', async event => {
  event.preventDefault(); output.textContent = 'Calculating…';
  const payload = { operation: selected.id };
  new FormData(form).forEach((value, key) => { payload[key] = Number(value); });
  try {
    const response = await fetch('/api/calculate', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)});
    const body = await response.json();
    output.textContent = response.ok ? `${selected.label}: ${body.result}` : body.error;
  } catch (_) { output.textContent = 'The calculator is unavailable. Please try again.'; }
});

drawInputs();
