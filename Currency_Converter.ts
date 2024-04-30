import inquirer from 'inquirer'
// join whatsap chennal: https://whatsapp.com/channel/0029VaDV3lsADTOK3izlJx0p
// youtube: @GenAi14
// discord : najafali14
async function Currency_Converter() {
  while (true) {

    let { Amount, exchangeTo } = await inquirer.prompt([
      {
        'type': 'number',
        'name': 'Amount',
        'message': 'Enter the amount in PKR: '
      },
      {
        'type': 'list',
        'name': 'exchangeTo',
        'message': 'exchangeTo',
        'choices': ['USD', 'INR', 'CNY', 'QAR', 'SAR', 'AED']
      }
    ])
    // pkr to other
    if (exchangeTo == 'USD') {
      console.log(Amount / 280, 'USD')
    }
    else if (exchangeTo == 'INR') {
      console.log(Amount / 3, 'INR')
    }
    else if (exchangeTo == 'CNY') {
      console.log(Amount / 38, 'CNY')
    }
    else if (exchangeTo == 'QAR') {
      console.log(Amount / 76, 'QAR')
    }
    else if (exchangeTo == 'SAR') {
      console.log(Amount / 74, 'SAR')
    }
    else if (exchangeTo == 'AED') {
      console.log(Amount / 75, 'AED')
    }
// increase conditions for more curruncies or from curruncy
    else {
      console.log('Invalid')
    }
  }

}
Currency_Converter()
