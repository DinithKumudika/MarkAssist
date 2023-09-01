import classnames from "classnames";
import Table from "./Table";
function Papers({clicked,data}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px] px-4');
  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner'}`}>
      <p className="text-center text-[#191854] text-xl font-bold mb-4">Marks</p>
      {/* <p className="text-center font-medium">Check your marking scheme and deselect the unnecessary selections</p> */}
      <Table index={true} fileName={true} overallMark={true} papers={data}/>
    </div>
  )
}

export default Papers
