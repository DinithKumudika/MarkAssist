function MarkAccurcyConfigureBox({handleAddChild,handleRemoveChild,index,data,addMinus,handleFormChange}) {
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
    const updatedFormData = { ...data, [name]: value };
    handleFormChange(index, updatedFormData);
  };
  return (
    <div className="flex flex-row justify-between mb-2">
      <input min="0" max="100" className="w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[60px]" type="text" name="minimum" value={`${data.minimum}`} disabled/>
      <input min="0" max="100" onChange={handleInputChange} className="w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[75px]" type="number" name="maximum" value={`${data.maximum}`}/>
      <input min="0" max="100" onChange={handleInputChange} className="w-[150px] bg-custom-gray-1 text-center rounded py-1 mr-2 max-md:w-[60px]" type="number" name="marks" value={data.marks}/>
      <div onClick={handleClick}>
        <input onClick={handleClick} className="bg-custom-gray-1 text-center rounded py-1 w-[36px] font-bold" type="text" name="" value={addMinus} disabled />
      </div>
    </div>
  )
}

export default MarkAccurcyConfigureBox
