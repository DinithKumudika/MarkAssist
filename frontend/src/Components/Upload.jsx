import DragDrop2 from './DragDrop'
import classnames from 'classnames'
function Upload({clicked}) {
  const classes = classnames('sidebar static max-sm:ml-16');
  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner'}`}>
      <DragDrop2/>
    </div>
  )
}

export default Upload
