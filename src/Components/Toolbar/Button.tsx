import React from 'react';

type ButtonProps = {
	icon: string;
	onclick?: React.MouseEventHandler<HTMLButtonElement>;
	data?: {
		toggle: string,
		target: string
	};
};

type RadioButtonProps = {
	id: string;
	icon: string;
	checked: boolean;
};

const Button = (props: ButtonProps): JSX.Element => {
	return (
		<button type="button" className="btn btn-primary" onClick={props.onclick}>
			<i className="material-icons">
				{props.icon}
			</i>
		</button>
	);
};

const RadioButton = (props: RadioButtonProps): JSX.Element => {
	return (
		<label className="btn btn-primary form-check-label">
			<input className="form-check-input" name="select-editor" id={props.id} type="radio" autoComplete="off" 
				   checked={props.checked} readOnly/>
			<i className="material-icons">
				{props.icon}
			</i>
		</label>
	);
};

const RefreshButton = (): JSX.Element => {
	return (
		<a className="btn btn-primary" href="/git_pull" role="button">
			<i className="material-icons">
				autorenew
			</i>
		</a>
	);	
}

export { Button, RadioButton, RefreshButton };