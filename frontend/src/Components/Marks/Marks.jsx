import MarksBox from "./MarksBox"
import classnames from 'classnames';
function Marks({clicked}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');

  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner'}`}>
      <p className="text-center text-[#191854] text-xl font-bold">Marking Scheme</p>
      <p className="text-center font-medium">Check your marking scheme and deselect the unnecessary selections</p>
      <MarksBox data="hello" />
      <MarksBox data="hello" />
      <MarksBox data="hello" />
    </div>
  )
}

export default Marks
