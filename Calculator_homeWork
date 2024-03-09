import inquirer from 'inquirer';
// functions creations for calculator
async function calculator(){
  let {num1,num2, op} = await inquirer.prompt([
    {
      type: 'input',
      name: 'num1',
      message: 'Enter first number: '
    },
    {
      type: 'input',
      name: 'num2',
      message: 'Enter second number: '
    },
    {
      type: 'input',
      name: 'op',
      message: 'Enter operator: '
    }
  ])
// apply conditions
  if (op=='+'){
    console.log(parseInt(num1)+parseInt(num2))
  } else if(op=='-'){
    console.log(num1-num2)
  } else if(op=='*'){
    console.log(num1*num2)
  } else if(op=='/'){
    console.log(num1/num2)
  } else if(op=='%'){
    console.log(num1%num2)
  } else{
    console.log('Please try again')
  }
  
}
// cal function
calculator()
