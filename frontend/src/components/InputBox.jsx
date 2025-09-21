function InputBox(props) {
    return (
        <div>
            <label htmlFor={props.htmlFor}>
                {props.label}
            </label>

            <input className={props.className}
                type={props.type} 
                id={props.htmlFor} 
                name={props.htmlFor} 
                placeholder={props.placeholder} 
                onChange={props.onChange}
            />
        </div>
    );
}

export default InputBox;