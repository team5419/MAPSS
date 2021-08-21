import ButtonGroup from './ButtonGroup';
import { Button, RadioButton, RefreshButton } from './Button';

import './button.css';

const Toolbar = (): JSX.Element => {
	const arrow_back_on_click = (): void => {
		window.location.href = 'https://team5419.org';
	};

	const add_item_on_click = (): void => {	
		/// TODO: Implement AddItem OnClick Event
	}

	const remove_item_on_click = (): void => {
		/// TODO: Implement RemoveItem OnClick Event
	}
	
	/// TODO: Figure Out What It Does
	const func_1 = (): void => {

	}

	/// TODO: Figure Out What It Does
	const func_2 = (): void => {

	}

	const google_sheets_on_click = (): void => {
		window.open('https://docs.google.com/spreadsheets/d/1Kjpfi7TuhB7UbsIvLi3TQMrF0fJYwV-d2gq1PZ3EVf4/edit#gid=0');
	}

	const github_on_click = (): void => {
		window.open('https://github.com/lemmaammel/itemSorter');
	}

	return (
		<ButtonGroup classes="btn-toolbar d-flex justify-content-center" role="toolbar">
			<ButtonGroup classes="btn-group mr-auto" role="group">
				<Button icon="arrow_back" onclick={arrow_back_on_click}/>
			</ButtonGroup>
			<ButtonGroup classes="btn-group mr-3" data_toggle="buttons" role="group">
				<RadioButton id="edit-marker-btn" icon="place" checked={true}/>
				<RadioButton id="edit-container-btn" icon="check_box_outline_blank" checked={false}/>
			</ButtonGroup>
			<ButtonGroup classes="btn-group mr-3" role="group">
				<Button icon="add_circle_outline" onclick={add_item_on_click}/>
				<Button icon="remove_circle_outline" onclick={remove_item_on_click}/>
				<Button icon="open_with" onclick={func_1}/>
				<Button icon="edit" onclick={func_2}/>
			</ButtonGroup>
			<ButtonGroup classes="btn-group mr-3" role="group">
				<Button icon="search" data={{ toggle: "modal", target: "#locateItemModal" }}/>
			</ButtonGroup>
			<ButtonGroup classes="btn-group ml-auto" role="group">
				<RefreshButton/>
				<Button icon="view_list" onclick={google_sheets_on_click}/>
				<Button icon="info" onclick={github_on_click}/>
			</ButtonGroup>
		</ButtonGroup>
	)
};

export default Toolbar;