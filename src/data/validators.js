export function isTermChecked(value) {
  return value
}

export function isInvoiceChecked(value) {
  value = document.querySelector("input[id=invoice]").checked
  return value
}
