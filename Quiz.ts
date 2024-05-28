// easiest way to create Quiz project in typescript
import inquirer from 'inquirer'
// creating main quiz function
async function Quiz(){ // quiz function start
  let score = 0;
  let wrong = 0
  let questions = await inquirer.prompt([
    {
      
      'message': 'what is capital of pakistan?',
      'name': 'q1',
      'type': 'list',
      'choices': ['karachi','multan','islamabad','lahore']
    },
    {

      'message': 'largest city in pakistan?',
      'name': 'q2',
      'type': 'list',
      'choices': ['karachi','multan','islamabad','lahore']
    },
    {

      'message': 'in which city minor e pakistan is located?',
      'name': 'q3',
      'type': 'list',
      'choices': ['karachi','multan','islamabad','lahore']
    },
    {

      'message': 'which city of pakistan is famous for sohn halwa?',
      'name': 'q4',
      'type': 'list',
      'choices': ['karachi','multan','islamabad','lahore']
    },
    {

      'message': 'which city of pakistan is famous for mangoes?',
      'name': 'q5',
      'type': 'list',
      'choices': ['karachi','multan','islamabad','muzaffargarh']
    },
  ])
  if (questions.q1==='islamabad'){ // first if start
    score = score+1;
    
  }
    else{
      wrong = wrong+1

      // console.log(questions.q1,'is wrong answer')

    }
    if (questions.q2==='karachi'){ // 2 if start
      score = score+1;
      // console.log(score)
    }
      else{
        wrong = wrong+1

        // console.log(questions.q2,'is wrong answer')

      }
      if (questions.q3==='lahore'){ // 3 if start
        score = score+1;
        // console.log(score)
      }
        else{
          wrong = wrong+1

          // console.log(questions.q3,'is wrong answer')

        }
        if (questions.q4==='multan'){ // 4 if start
          score = score+1;
          // console.log(score)
        }
          else{
            wrong = wrong+1

            // console.log(questions.q4,'is wrong answer')

          }
          if (questions.q5==='muzaffargarh'){ // 5 if start
            score = score+1;
          }
            else{
              
              // console.log(questions.q5,'is wrong answer')
              wrong = wrong+1
              

            }
  // printing result
  console.log('total scores: ',score)

  console.log('wrong answers: ', wrong)
    
} // quiz function end
Quiz()// calling  quiz function
