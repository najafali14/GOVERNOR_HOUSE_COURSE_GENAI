
// # Explanation Video: https://youtu.be/41hGqZD5qY8

import inquirer from 'inquirer';
import chalk from 'chalk';
// functions creations for BMI calculator
async function calculator(){
  let {weight,height} = await inquirer.prompt([
    {
      type: 'input',
      name: 'weight',
      message: chalk.bgGreen('Enter your weight: \n') //in kilograms
    },
    {
      type: 'input',
      name: 'height',
      message: chalk.bgGreen('Enter your height: \n') //in meters
    }
  ])
console.log(chalk.red(weight/height**2))

}
// cal function
calculator()
