import MarksBox from "./MarksBox"
import classnames from 'classnames';
function Marks({clicked}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  const answersheets = JSON.parse(localStorage.getItem('answers'));
  const markingschemes = JSON.parse(localStorage.getItem('markingSceme'));
  console.log(answersheets)
  console.log(markingschemes)

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <p className="text-center text-[#191854] text-xl font-bold">Marking Scheme</p>
      <p className="text-center font-medium">Check your marking scheme and deselect the unnecessary selections</p>
      <MarksBox data="hello" markingScheme_URL={markingschemes.marking_urls[0]} answersheet_URL={answersheets.data[0]} />
      <MarksBox data="hello" markingScheme_URL={markingschemes.marking_urls[1]} answersheet_URL={answersheets.data[1]} />
      <MarksBox data="hello" markingScheme_URL={markingschemes.marking_urls[2]} answersheet_URL={answersheets.data[2]} />
      <MarksBox data="hello" markingScheme_URL={markingschemes.marking_urls[3]} answersheet_URL={answersheets.data[3]} />
    </div>
  )
}

export default Marks
