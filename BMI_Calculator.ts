import inquirer from 'inquirer';
// functions creations for calculator
async function calculator(){
  let {weight,height} = await inquirer.prompt([
    {
      type: 'input',
      name: 'weight',
      message: 'Enter your weight: ' //in kilograms
    },
    {
      type: 'input',
      name: 'height',
      message: 'Enter your height: ' //in meters
    }
  ])
console.log(weight/height**2)

}
// cal function
calculator()
