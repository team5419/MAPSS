import React from 'react';

type ButtonGroupProps = {
	classes: string
	children: React.ReactNode
	data_toggle?: string
	role?: string
};

const ButtonGroup = (props: ButtonGroupProps): JSX.Element => {
	return (
		<section className={props.classes}
				 data-toggle={ props.data_toggle !== undefined ? props.data_toggle : "" }
				 role={props.role !== undefined ? props.role : ""}>
			{props.children}
		</section>
	);
};

export default ButtonGroup;