import classnames from 'classnames'
function Button({children,classNames,onClick}) {
  return (
    <div className={`${classNames} bg-[#3443C9] rounded-[5px] text-white font-bold p-1 px-4 cursor-pointer`} onClick={onClick}>
      {children}
    </div>
  )
}

export default Button
