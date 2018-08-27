import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css'
import {
    Row, Col, Card, CardBody, CardImg, CardTitle, CardText,
} from 'reactstrap';
import './index.css'

class YNB extends React.Component {
    constructor() {
        super(); //Whenever constructor is called, you must also call super like so.

        this.state = {
            'items': []
        }
    }
    componentDidMount() {
        this.getItems();

    }

    getItems() {
        fetch('http://127.0.0.1:8000/books/api/books/')
            .then(results => results.json())
            .then(results => this.setState({'items': results}));
    }
    render() {
        return (
            <ul>
                {this.state.items.map(function (item, index) {
                    return (
                        <ContentItem item={item} key={index} /*solves key/prop issue*/ />

                    )
                }
                )}
            </ul>
        );
    }
}


class ContentItem extends React.Component {
        render() {
            return (
                <Row className="ContentItem">
                    <Col xs="3"></Col>
                        <Col xs="6">
                        <Card>
                            <CardImg top width="100%"
                                     src={this.props.item.image}></CardImg>
                            <CardBody>
                                <CardTitle>
                                    {this.props.item.title}
                                </CardTitle>
                                <CardText>
                                    {this.props.item.content}
                                </CardText>
                            </CardBody>
                        </Card>
                    </Col>
                </Row>
            )
        }
    }


ReactDOM.render(
    <YNB />,
    document.getElementById('root')
)