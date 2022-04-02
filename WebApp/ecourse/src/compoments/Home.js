import React from 'react';
import { Card, Col, Container, Row } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <Container>
            <h1 className="text-center text-danger">DANH MUC KHOA HOC</h1>
            <Row>
                <Col md={4}>
                <Card>
                    <Card.Img variant="top" fluid="true" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                    <Card.Body>
                        <Card.Text>Cong nghe phan mem</Card.Text>
                        <Link to="/courses/1/lessons" className="btn btn-info">Cac bai hoc</Link>
                    </Card.Body>
                </Card>
                </Col>

                <Col md={4}>
                <Card>
                    <Card.Img variant="top" fluid="true" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                    <Card.Body>
                        <Card.Text>Cong nghe phan mem</Card.Text>
                        <Link to="/courses/1/lessons" className="btn btn-info">Cac bai hoc</Link>
                    </Card.Body>
                </Card>
                </Col>

                <Col md={4}>
                <Card>
                    <Card.Img variant="top" fluid="true" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                    <Card.Body>
                        <Card.Text>Cong nghe phan mem</Card.Text>
                        <Link to="/courses/1/lessons" className="btn btn-info">Cac bai hoc</Link>
                    </Card.Body>
                </Card>
                </Col>
            </Row>
        </Container>
    )
}

export default Home