import datetime

from django.test import TestCase
from django.test import SimpleTestCase

from test_contacts import CustomContactAssertions
from models import FboMaster
from parser import parse_file
import parse_helpers


class TestParser(TestCase):

    @classmethod
    def setUpClass(cls):

        test_file_path = 'fbo/presol.txt'
        parse_file(test_file_path)
        cls.master = FboMaster.objects.all()[0]

    @classmethod
    def tearDownClass(cls):
        FboMaster.objects.all().delete()
        pass

    def test_date(self):
        self.assertEqual(self.master.date, datetime.date(16, 11, 4))

    def test_agency(self):
        self.assertEqual(self.master.agency ,'Department of the Air Force')

    def test_office(self):
        self.assertEqual(self.master.office ,'AFICA')

    def test_location(self):
        self.assertEqual(self.master.location ,'AFICA- CONUS')

    def test_class_code(self):
        self.assertEqual(self.master.class_code ,'U')

    def test_naics(self):
        self.assertEqual(self.master.naics ,'611699')

    def test_office_address(self):
        self.assertEqual(self.master.office_address ,'Test Office Address')

    def test_subject(self):
        self.assertEqual(self.master.subject , r'AFICA Battlefield Airman (BA) Military Freefall (MFF)')

    def test_solnbr(self):
        self.assertEqual(self.master.solnbr , 'FA3002-16-R-0023')

    def test_response_date(self):
        self.assertEqual(self.master.response_date ,datetime.date(16, 11, 21))

    def test_description(self):
        answer = r'<strong>Requirement Summary:</strong><span style="mso-spacerun: yes">&nbsp; </span>This requirement is for Military Freefall (MFF) training for Battlefield Airman (BA) personnel. MFF training is an initial skills course that provides academic, ground, vertical wind tunnel/simulation, and military freefall training to first time jumpers that meets United States Special Operations Command/United States Army Special Operations Command (USSOCOM/USASOC) curriculum requirements.<span style="mso-spacerun: yes">&nbsp; </span><p>The United States Air Force (USAF) requires instructional support and training services in the delivery of MFF parachutist training.<span style="mso-spacerun: yes">&nbsp; </span>These services will include fully qualified MFF instructors and Contractor personnel to provide the instructional support and training services typically associated with the delivery of the AF MFF Parachutist Course (MFFPC).<span style="mso-spacerun: yes">&nbsp; </span></p><p><strong>Request for Information:</strong><span style="mso-spacerun: yes">&nbsp; </span>This is a Follow-On Request for Information (RFI).<span style="mso-spacerun: yes">&nbsp; </span>Responses to this notice are not offers and cannot be accepted by the Government to form a binding contract.<span style="mso-spacerun: yes">&nbsp;&nbsp; <strong><span style="text-decoration: underline;">Responses are due NLT 3:00&nbsp;pm CST on 21 Nov 16.</span></strong> </span>Please see the following attached documents for all information pertaining to this RFI:</p><p>1.<span style="mso-tab-count: 1">&nbsp; </span>BA MFF - Follow-on RFI<span style="mso-spacerun: yes">&nbsp; </span>- 04 Nov 16<br />2.&nbsp; Attachment 1 - Draft BA MFF PWS - 04 Nov 16<br />3.&nbsp; Attachment 2 - Draft Section L<br />4.&nbsp; Attachment 3 - Draft Section M<br />5.&nbsp; Attachment 4 - Draft Pricing Model</p><p><strong>NOTE:</strong><span style="mso-spacerun: yes">&nbsp; </span>This requirement was previously combined with Battlefield Airman Aircraft Lift Service Requirement and market research was performed for this requirement under the following FBO Link:<br /><a href="https://www.fbo.gov/notices/0b92fc8041dfb6398916a36bf65d7c43">https://www.fbo.gov/notices/0b92fc8041dfb6398916a36bf65d7c43</a></p><p>However, The Battlefield Airman Military Freefall (MFF) and Aircraft Lift Service Requirements have been separated into two separate contract actions.<span style="mso-spacerun: yes">&nbsp; </span>This link is only for the Battlefield Airman (BA) Military Freefall (MFF) requirement.</p>'

        self.assertEqual(self.master.description, answer)

    # def test_link(self):
        # self.assertEqual(self.master. ,)

    def test_setaside(self):
        self.assertEqual(self.master.setaside, 'N/A')

    def test_popaddress(self):
        self.assertEqual(self.master.pop_address, 'TBD')

    def test_popcountry(self):
        self.assertEqual(self.master.pop_country, 'US')

class TestMultiLineContact(TestCase, CustomContactAssertions):
    @classmethod
    def setUpClass(cls):
        test_file_path = 'fbo/test_files/multi_line_contacts.txt'
        parse_file(test_file_path)
        cls.master = FboMaster.objects.all()[0]

    def test_contacts(self):

        # Reminder to check the description on this one

        answer = [
            Contact(
                name = 'Hal Hayes',
                phone = '6195321251',
                title = 'Contract Specialist',
                email = 'harold.hayes@navy.mil',
            )
        ]
        self.assertContactsEqual(answer, master.contacts)


class TestHelpers(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.master = FboMaster()
        cls.master.save()

    @classmethod
    def tearDownClass(cls):
        FboMaster.objects.all().delete()
        pass

    def test_date(self):
        month_day_line = '1104'
        year_line = '16'
        parse_helpers.date(self.master, month_day_line)
        parse_helpers.year(self.master, year_line)
        self.assertEqual(self.master.date, datetime.date(16, 11, 4))

    def test_respdate(self):
        line = '112116'
        parse_helpers.respdate(self.master, line)
        self.assertEqual(self.master.response_date, datetime.date(16, 11, 21))
