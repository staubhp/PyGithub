# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitBlobAttributes(TestCase):
    def test(self):
        b = self.electra.get_repo(("electra", "git-objects")).get_git_blob("3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(b.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
        self.assertEqual(b.encoding, "base64")
        self.assertEqual(b.mode, None)
        self.assertEqual(b.path, None)
        self.assertEqual(b.size, 20)
        self.assertEqual(b.type, None)
        self.assertEqual(b.url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/git/blobs/3daf0da6bca38181ab52610dd6af6e92f1a5469d")

    def testInTree(self):
        b = self.electra.get_repo(("electra", "git-objects")).get_git_tree("f2b2248a59b245891a16e7d7eecfd7bd499e4521").tree[0]
        self.assertEqual(b.mode, "100644")
        self.assertEqual(b.path, "a_blob")
        self.assertEqual(b.type, "blob")
        self.assertEqual(b.url, "http://github.home.jacquev6.net/api/v3/repos/electra/git-objects/git/blobs/3daf0da6bca38181ab52610dd6af6e92f1a5469d")


class GitBlobUpdate(TestCase):
    def testThroughLazyCompletion(self):
        b = self.electra.get_repo(("electra", "git-objects")).create_git_blob("This is some content", "utf8")
        b._UpdatableGithubObject__eTag = None  # @todoAlpha All create_xxx function should return lazy-completable objects
        self.assertEqual(b.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(b.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")

    def test(self):
        b = self.electra.get_repo(("electra", "git-objects")).create_git_blob("This is some content", "utf8")
        self.assertEqual(b.content, None)
        self.assertTrue(b.update())
        self.assertFalse(b.update())
        self.assertEqual(b.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
