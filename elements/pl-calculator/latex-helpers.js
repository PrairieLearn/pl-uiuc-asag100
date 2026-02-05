/**
 * @param {string} input
 */
export function containsTrigFunction(input) {
  return /sin|cos|tan|cot|sec|csc/i.test(input);
}
