function MarkAccurcyConfigureBox({handleAddChild,handleRemoveChild,index,data,add, Minus,handleFormChange}) {
  const handleClick = (event) => {
    const val = event.target.value
    if(val==="+"){
      console.log("+",index)
      handleAddChild();
    }else if(val==="-"){
      console.log("-",index)
      handleRemoveChild(index);
    }
  }

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    const updatedFormData = { ...data, [name]: parseInt(value) };
    // console.log(updatedFormData)
    handleFormChange(index, updatedFormData);
  };
  return (
    <div className="flex flex-row justify-between mb-2">
      <input min="0" max="100" className="w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[60px]" type="number" name="minimum" value={data.minimum} disabled/>
      <input min="0" max="100" onChange={handleInputChange} className="w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[75px]" type="number" name="maximum" value={data.maximum}/>
      <input min="0" max="100" onChange={handleInputChange} className="w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[60px]" type="number" name="percentageOfMarks" value={data.percentageOfMarks}/>
      <div onClick={handleClick}>
      <input onClick={handleClick} className="hover:cursor-pointer bg-custom-gray-1 text-center rounded py-1 w-[36px] font-bold mr-2" type="text" name="" value={add} disabled />
      <input onClick={handleClick} className="hover:cursor-pointer bg-custom-gray-1 text-center rounded py-1 w-[36px] font-bold" type="text" name="" value={Minus} disabled />
      </div>
    </div>
  )
}

export default MarkAccurcyConfigureBox
