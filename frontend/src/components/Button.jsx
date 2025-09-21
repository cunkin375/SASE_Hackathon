function Button(props) {
    return (
        <button 
            className={props.className}
            onClick={props.onClick}
            type={props.type || "button"}
        >
            {props.name}
        </button>
    );
}

export default Button;