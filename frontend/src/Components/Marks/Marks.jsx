import MarksBox from "../MarksBox"
import classnames from 'classnames';
function Marks({clicked}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[8%]');

  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner'}`}>
      <MarksBox />
    </div>
  )
}

export default Marks
