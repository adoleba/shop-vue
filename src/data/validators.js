import {Store} from "../store/store";

export function isTermChecked(value) {
  return value
}

export function isPrivatePerson() {
  if (Store.state.customerKind === 'privatePerson') {
    return true
  } else {
    return false
  }
}

export function isCompany() {
  if (Store.state.customerKind === 'company') {
      return true
  } else {
    return false
  }
}