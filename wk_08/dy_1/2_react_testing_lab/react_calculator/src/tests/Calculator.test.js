import React from 'react';
import Calculator from '../containers/Calculator';
import {render, fireEvent} from '@testing-library/react';

describe('Calculator', () => {
  let container;
  beforeEach(() => {
    container = render(<Calculator/>)
  })

  it('should change running total on number enter', () => {
    const button4 = container.getByTestId('number4');
    const runningTotal = container.getByTestId('running-total');
    fireEvent.click(button4);
    expect(runningTotal.textContent).toEqual('4');
  })

  it('should add 1 to 4 and get 5', () => {
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('0')
    const button1 = container.getByTestId('number1');
    const button4 = container.getByTestId('number4');
    const operatorAdd = container.getByTestId('operator-add')
    const operatorEquals = container.getByTestId('operator-equals')
    fireEvent.click(button1)
    expect(runningTotal.textContent).toEqual('1')
    fireEvent.click(operatorAdd)
    fireEvent.click(button4)
    fireEvent.click(operatorEquals)
    expect(runningTotal.textContent).toEqual('5')

  })

  it('should subtract 4 from 7 and get 3', () => {
    const runningTotal = container.getByTestId('running-total')
    expect(runningTotal.textContent).toEqual('0')
    const button7 = container.getByTestId('number7')
    const button4 = container.getByTestId('number4')
    const operatorSubtract = container.getByTestId('operator-subtract')
    const operatorEquals = container.getByTestId('operator-equals')
    fireEvent.click(button7)
    fireEvent.click(operatorSubtract)
    fireEvent.click(button4)
    fireEvent.click(operatorEquals)
    expect(runningTotal.textContent).toEqual('3')
  })

  it('should multiply 3 by 5 and get 15', () => {
    const runningTotal = container.getByTestId('running-total')
    const button3 = container.getByTestId('number3')
    const button5 = container.getByTestId('number5')
    const operatorMultiply = container.getByTestId('operator-multiply')
    const operatorEqual = container.getByTestId('operator-equals')
    fireEvent.click(button3)
    fireEvent.click(operatorMultiply)
    fireEvent.click(button5)
    fireEvent.click(operatorEqual)
    expect(runningTotal.textContent).toEqual('15')
  })

  it('should divide 21 by 7 and get 3', () => {
    const runningTotal = container.getByTestId('running-total')
    const button2 = container.getByTestId('number2')
    const button1 = container.getByTestId('number1')
    const button7 = container.getByTestId('number7')
    const operatorDivide = container.getByTestId('operator-divide')
    const operatorEquals = container.getByTestId('operator-equals')
    fireEvent.click(button2)
    fireEvent.click(button1)
    fireEvent.click(operatorDivide)
    fireEvent.click(button7)
    fireEvent.click(operatorEquals)
    expect(runningTotal.textContent).toEqual('3')
  })

  it('should concatenate multiple number button clicks', () => {
    const runningTotal = container.getByTestId('running-total')
    const button1 = container.getByTestId('number1')
    expect(runningTotal.textContent).toEqual('0')
    fireEvent.click(button1)
    expect(runningTotal.textContent).toEqual('1')
    fireEvent.click(button1)
    expect(runningTotal.textContent).toEqual('11')
    fireEvent.click(button1)
    expect(runningTotal.textContent).toEqual('111')

  })

  it('should chain multiple operations together', () => {
    const button2 = container.getByTestId('number2')
    const operatorMultiply = container.getByTestId('operator-multiply')
    const operatorEquals = container.getByTestId('operator-equals')
    const runningTotal = container.getByTestId('running-total')
    fireEvent.click(button2)
    fireEvent.click(operatorMultiply)
    fireEvent.click(button2)
    fireEvent.click(operatorMultiply)
    fireEvent.click(operatorEquals)
    expect(runningTotal.textContent).toEqual('8')
  })

  it('should clear the running total without affecting the calculation', () => {
    const button3 = container.getByTestId('number3')
    const operatorAdd = container.getByTestId('operator-add')
    const operatorMultiply = container.getByTestId('operator-multiply')
    const operatorEquals = container.getByTestId('operator-equals')
    const operatorClear  = container.getByTestId('clear')
    const runningTotal = container.getByTestId('running-total')

    fireEvent.click(button3)
    fireEvent.click(operatorAdd)
    fireEvent.click(button3)
    fireEvent.click(operatorEquals)
    expect(runningTotal.textContent).toEqual('6')
    fireEvent.click(operatorClear)
    fireEvent.click(operatorClear)  
    expect(runningTotal.textContent).toEqual('0')
    fireEvent.click(button3)
    expect(runningTotal.textContent).toEqual('3')
    fireEvent.click(operatorMultiply)
    fireEvent.click(button3)
    fireEvent.click(operatorEquals)
    expect(runningTotal.textContent).toEqual('9')

  })

})

