import MarksBox from "./MarksBox"
import classnames from 'classnames';
function Marks({clicked,answers,markings}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  // const answersheets = JSON.parse(localStorage.getItem('answers'));
  // const markingschemes = JSON.parse(localStorage.getItem('markingSceme'));
  // console.log(answers)
  // console.log(markings)

  const data = answers.map((answer, index) => (
      <MarksBox
        key={answer.id}
        markingScheme_URL={markings[index].uploadUrl}
        answersheet_URL={answer.uploadUrl}
      />
      // console.log(markings[index])
    ));

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <p className="text-center text-[#191854] text-xl font-bold">Marking Scheme</p>
      <p className="text-center font-medium">Check your marking scheme and deselect the unnecessary selections</p>
      {data}
    </div>
  )
}

export default Marks
