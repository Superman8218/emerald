from django.test import TestCase

from parse_helpers import extract_contacts
import parse_helpers
from contact.models import Contact

import pdb

class CustomContactAssertions:
    def assertContactsEqual(self, input_list, answer_list):
        if len(input_list) != len(answer_list):
            raise AssertionError('Number of contacts differ between lists.')

        for x in xrange(0, len(input_list)):
            if input_list[x].name != answer_list[x].name:
                msg = 'Element number {0}, name differs between the sets'.format(x)
                raise AssertionError(msg)
            if input_list[x].title != answer_list[x].title:
                msg = 'Element number {0}, title differs between the sets'.format(x)
                raise AssertionError(msg)
            if input_list[x].phone != answer_list[x].phone:
                msg = 'Element number {0}, phone differs between the sets'.format(x)
                raise AssertionError(msg)
            if input_list[x].email != answer_list[x].email:
                msg = 'Element number {0}, email differs between the sets'.format(x)
                raise AssertionError(msg)
            if input_list[x].fax != answer_list[x].fax:
                msg = 'Element number {0}, fax differs between the sets'.format(x)
                raise AssertionError(msg)


class TestExtractContacts(TestCase, CustomContactAssertions):

    def test_normal(self):

        line = 'Tina L. Watsontarver, Contract Specialist, Email tina.watsontarver.1@us.af.mil, Phone (123)456-7890 - Jaclyn G. Rodriguez, Contracting Officer, Email jaclyn.rodriguez@us.af.mil'
        contacts = extract_contacts(line)

        tina = Contact(
            name='Tina L. Watsontarver',
            title='Contract Specialist',
            email='tina.watsontarver.1@us.af.mil',
            phone='1234567890',
        )

        jaclyn = Contact(
            name='Jaclyn G. Rodriguez',
            title='Contracting Officer',
            email='jaclyn.rodriguez@us.af.mil'
        )

        answer = [tina, jaclyn]

        self.assertContactsEqual(answer, contacts)

    def test_name_phone_without_space(self):
        line = 'Test Person123-456-7890'
        contacts = extract_contacts(line)
        person = Contact(
            name='Test Person',
            phone='1234567890',
        )
        answer = [person]
        self.assertContactsEqual(answer, contacts)

    def test_name_phone_with_space(self):
        line = 'Test Person (123)-456-7890'
        contacts = extract_contacts(line)
        person = Contact(
            name='Test Person',
            phone='1234567890',
        )
        answer = [person]
        self.assertContactsEqual(answer, contacts)

    def test_first_last(self):
        line = 'Test Person'
        contacts = extract_contacts(line)
        one = Contact(
            name='Test Person'
        )
        answer = [one]
        self.assertContactsEqual(answer, contacts)

    def test_last_comma_first(self):
        line = 'Sixon, Antonio C.'
        contacts = extract_contacts(line)
        one = Contact(
            name='Antonio C. Sixon'
        )
        answer = [one]
        self.assertContactsEqual(answer, contacts)

    def test_semicolon_phone(self):
        line = 'Carolyn M. Blake 817-978-4661  ; Kelly M Pippin 817-850-5774'
        contacts = extract_contacts(line)
        carolyn = Contact(
            name='Carolyn M. Blake',
            phone='8179784661',
        )
        kelly = Contact(
            name='Kelly M Pippin',
            phone='8178505774',
        )
        answer = [carolyn, kelly]
        self.assertContactsEqual(answer, contacts)

    def test_email_only(self):
        line = 'zac.yauney@gmail.com'
        contacts = extract_contacts(line)
        one = Contact(
            email='zac.yauney@gmail.com'
        )
        answer = [one]
        self.assertContactsEqual(answer, contacts)

class TestFormatName(TestCase):
    def test_normal(self):
        person = 'Tina L. Watsontarver, Contract Specialist, Email tina.watsontarver.1@us.af.mil, Phone (123)456-7890'
        formatted_person = parse_helpers.format_name(person)
        answer = 'Name: Tina L. Watsontarver, Contract Specialist, Email tina.watsontarver.1@us.af.mil, Phone (123)456-7890'
        self.assertEqual(formatted_person, answer)

    def test_email_only(self):
        person = 'zac.yauney@gmail.com'
        formatted_person = parse_helpers.format_name(person)
        self.assertEqual(formatted_person, person)

    def test_name_phone_without_space(self):
        person = 'Test Person1234567890'
        formatted_person = parse_helpers.format_name(person)
        answer = 'Name: Test Person, Phone: 1234567890'
        self.assertEqual(formatted_person, answer)

    def test_name_phone_with_space(self):
        person = 'Test Person 1234567890'
        formatted_person = parse_helpers.format_name(person)
        answer = 'Name: Test Person, Phone: 1234567890'
        self.assertEqual(formatted_person, answer)

    def test_last_comma_first(self):
        person = 'Person, Test M.'
        formatted_person = parse_helpers.format_name(person)
        answer = 'Name: Test M. Person'
        self.assertEqual(formatted_person, answer)

class TestFormatTitle(TestCase):
    def test_normal(self):
        person = 'Name: Tina L. Watsontarver,Contract Specialist,Email tina.watsontarver.1@us.af.mil,Phone (123)456-7890'
        formatted_person = parse_helpers.format_title(person)
        answer = 'Name: Tina L. Watsontarver,Title: Contract Specialist,Email tina.watsontarver.1@us.af.mil,Phone (123)456-7890'
        self.assertEqual(formatted_person, answer)

    def test_long(self):
        person = 'Name: Tina L. Watsontarver,Lease Contract Specialist,Email tina.watsontarver.1@us.af.mil,Phone (123)456-7890'
        formatted_person = parse_helpers.format_title(person)
        answer = 'Name: Tina L. Watsontarver,Title: Lease Contract Specialist,Email tina.watsontarver.1@us.af.mil,Phone (123)456-7890'
        self.assertEqual(formatted_person, answer)
